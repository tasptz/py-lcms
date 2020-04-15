import numpy as np
from . import pylcms
from .pylcms import Transformer

__version__ = '0.3.0'

def apply_profile(input_image, input_profile, output_profile='srgb', in_place=False):
    if in_place:
        if not input_image.flags['C_CONTIGUOUS']:
            raise RuntimeError('Input not contiguous')
        output_image = input_image
    else:
        input_image = np.ascontiguousarray(input_image)
        output_image = np.ascontiguousarray(np.empty_like(input_image))
    pylcms.apply_profile(input_image, output_image, input_profile, output_profile)
    return output_image
    
