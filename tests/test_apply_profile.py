import pytest

def test_identity_8():
    import numpy as np
    img = np.random.randint(0, 2**8 - 1, (256, 256, 3), np.uint8)
    from lcms import apply_profile
    img_t = apply_profile(img, 'srgb')
    assert np.array_equal(img, img_t)

def test_identity_16():
    import numpy as np
    img = np.random.randint(0, 2**16 - 1, (256, 256, 3), np.uint16)
    from lcms import apply_profile
    img_t = apply_profile(img, 'srgb')
    assert np.array_equal(img, img_t)

def test_identity_flt():
    import numpy as np
    img = np.random.rand(4, 4, 3).astype(np.float32)
    from lcms import apply_profile
    img_t = apply_profile(img, 'srgb')
    assert np.allclose(img, img_t)
