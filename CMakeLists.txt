cmake_minimum_required(VERSION 3.10)
project(pylcms LANGUAGES C CXX)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

add_subdirectory("${CMAKE_SOURCE_DIR}/ext/pybind11")

set(LITTLE_CMS_DIR "${CMAKE_SOURCE_DIR}/ext/Little-CMS")
file(GLOB src "${LITTLE_CMS_DIR}/src/*.c" "${LITTLE_CMS_DIR}/include/*.h")
add_library(lcms STATIC ${src} ${inc})
target_include_directories(lcms PUBLIC "${LITTLE_CMS_DIR}/include")

pybind11_add_module(pylcms MODULE module.cpp)
target_link_libraries(pylcms PRIVATE lcms)
if(DEFINED ENV{LCMS_THREADS})
    find_package(OpenMP REQUIRED)
    target_compile_definitions(pylcms PRIVATE "THREADS=$ENV{LCMS_THREADS}")
    target_link_libraries(pylcms PRIVATE OpenMP::OpenMP_CXX)
endif()
install(TARGETS pylcms DESTINATION lcms)