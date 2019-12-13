import numpy as np
from . import pylcms

__version__ = '0.1.0'

def apply_profile(input_image, input_profile, output_profile='srgb', in_place=False):
    if input_image.dtype != np.uint16:
        raise TypeError()
    if in_place:
        if not input_image.flags['C_CONTIGUOUS']:
            raise RuntimeError('Input not contiguous')
        output_image = input_image
    else:
        input_image = np.ascontiguousarray(input_image)
        output_image = np.ascontiguousarray(np.empty_like(input_image))
    pylcms.apply_profile(input_image, output_image, input_profile, output_profile)
    return output_image
    
