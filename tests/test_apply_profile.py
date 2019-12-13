import pytest

def test_identity():
    import numpy as np
    img = np.zeros((256, 256, 3), dtype=np.uint16)
    from lcms import apply_profile
    img_t = apply_profile(img, 'srgb')
    assert np.array_equal(img, img_t)
