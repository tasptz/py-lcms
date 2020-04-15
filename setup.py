from skbuild import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open('ReadMe.md') as f:
    description = f.read()

setup(
    name='lcms',
    version='0.3.0',
    description='A minimalistic module to utilize Little CMS (http://littlecms.com) to apply color profiles to 16 bit TIFF images',
    long_description=description,
    long_description_content_type='text/markdown',
    author='Thomas Pönitz',
    author_email='tasptz@gmail.com',
    url='https://github.com/tasptz/py-lcms',
    packages=['lcms'],
    install_requires=requirements,
    license='MIT',
    platforms=['any']
)