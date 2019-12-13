import cv2 as cv
import argparse
import lcms
from pathlib import Path

parser = argparse.ArgumentParser(description='Transform 16 bit TIFF image from one profile to another')
parser.add_argument('image', type=str, help='16 bit TIFF image to load')
parser.add_argument('source', type=str, help='Source color profile')
parser.add_argument('-d', '--destination', type=str, default='srgb', help='Destination color profile')
args = parser.parse_args()
rgb = cv.imread(args.image, cv.IMREAD_UNCHANGED)[..., ::-1]
rgb_t = lcms.apply_profile(rgb, args.source, args.destination)
cv.imwrite(str(Path(args.image).stem + '-transformed.tif'), rgb_t[..., ::-1])