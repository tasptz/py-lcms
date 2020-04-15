import pytest

def test_identity_8():
    import numpy as np
    img = np.ascontiguousarray(np.random.randint(0, 2**8 - 1, (256, 256, 3), np.uint8))
    img_t = np.ascontiguousarray(np.zeros_like(img))
    from lcms import Transformer
    t = Transformer('uint8', 'uint8', 'srgb', 'srgb')
    t.apply(img, img_t)
    assert np.array_equal(img, img_t)

def test_identity_16():
    import numpy as np
    img = np.ascontiguousarray(np.random.randint(0, 2**16 - 1, (256, 256, 3), np.uint16))
    img_t = np.ascontiguousarray(np.zeros_like(img))
    from lcms import Transformer
    t = Transformer('uint16', 'uint16', 'srgb', 'srgb')
    t.apply(img, img_t)
    assert np.array_equal(img, img_t)

def test_identity_flt():
    import numpy as np
    img = np.ascontiguousarray(np.random.rand(256, 256, 3).astype(np.float32))
    img_t = np.ascontiguousarray(np.zeros_like(img))
    from lcms import Transformer
    t = Transformer('float32', 'float32', 'srgb', 'srgb')
    t.apply(img, img_t)
    assert np.allclose(img, img_t)
