# Python Little CMS ![Travis CI build status](https://api.travis-ci.com/tasptz/py-lcms.svg?branch=master) [![PyPI version](https://badge.fury.io/py/lcms.svg)](https://badge.fury.io/py/lcms)
A minimalistic module to utilize [Little CMS](http://littlecms.com) to apply color profiles to 16 bit TIFF
images.

## Motivation
Currently there seems to be no python packages available to apply color profiles
to 16 bit TIFF images.
[Pillow](https://pillow.readthedocs.io/en/stable/reference/ImageCms.html) has
built in support for [Little CMS](http://littlecms.com), but does currently
not have [16 bit support](https://pillow.readthedocs.io/en/5.1.x/handbook/concepts.html#modes)
for RGB images.

## Installation
```
git submodule update --init
python setup.py bdist_wheel --build-type Release
```
Then install the wheel present in the `dist` folder.

## Example
To run the example you need a 16 bit TIFF image and a color profile, for example
a `*.icm` file.
Then run
```
python example.py your_image.tif your_profile.icm
```
and have a look at the generated image `your_image-transformed.tif`.
