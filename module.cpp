#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <lcms2.h>
#include <map>
#include <iostream>
#include <memory>

namespace py = pybind11;

struct Profile {
    Profile(cmsHPROFILE p) : p(p) { }
    Profile(Profile &&profile) { std::swap(p, profile.p); }
    ~Profile() {
        if (p)
            cmsCloseProfile(p);
    }
    cmsHPROFILE p = nullptr;
};

struct Transform {
    Transform(cmsHTRANSFORM t) : t(t) { }
    Transform(Transform &&transform) { std::swap(t, transform.t); }
    ~Transform() {
        if (t)
            cmsDeleteTransform(t);
    }
    cmsHTRANSFORM t = nullptr;
};

const std::map<std::string, std::function<Profile ()>> standardProfiles {
    {"srgb", []()->auto { return Profile(cmsCreate_sRGBProfile()); }}
};

Profile getProfile(const std::string &profileId) {
    try {
        Profile profile(cmsOpenProfileFromFile(profileId.c_str(), "r"));
        if (profile.p == nullptr) {
            return standardProfiles.at(profileId)();
        }
        return profile;
    }
    catch (std::out_of_range &) {
        throw py::key_error(profileId + " not found");
    }
}

const std::map<py::dtype, cmsUInt32Number> dataTypes {
    {py::dtype("uint8"), TYPE_RGB_8},
    {py::dtype("uint16"), TYPE_RGB_16},
    {py::dtype("float32"), TYPE_RGB_FLT}
};

cmsUInt32Number getDataType(const py::dtype &dtype) {
    try {
        return dataTypes.at(dtype);
    }
    catch (std::out_of_range &) {
        throw std::domain_error(std::string(py::str(static_cast<const py::object &>(dtype))) + " not implemented");
    }
}

void applyProfile(
        const py::array inputImage,
        py::array outputImage,
        const std::string &inputProfile,
        const std::string &outputProfile) {
    Profile ip(getProfile(inputProfile));
    Profile op(getProfile(outputProfile));
    cmsUInt32Number inputDataType = getDataType(inputImage.dtype());
    cmsUInt32Number outputDataType = getDataType(outputImage.dtype());
    Transform t(cmsCreateTransform(
        ip.p,
        inputDataType,
        op.p,
        outputDataType,
        INTENT_PERCEPTUAL,
        0
    ));
    cmsDoTransform(
        t.t,
        inputImage.data(0, 0, 0),
        outputImage.mutable_data(0, 0, 0),
        static_cast<cmsUInt32Number>(inputImage.shape(0) * inputImage.shape(1))
    );
}

PYBIND11_MODULE(pylcms, m) {
    m.def("apply_profile", &applyProfile);
}
