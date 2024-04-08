from setuptools import setup, find_packages
from shortwizard import __version__,    __app_name__

VERSION = __version__
DESCRIPTION = 'My first Python package'
LONG_DESCRIPTION = 'My first Python package with a slightly longer description'

with open('requirements.txt', 'r') as file:
    requirements = file.readlines()

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name=__app_name__, 
        version=VERSION,
        author="Jason Vannier",
        author_email="<youremail@email.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        include_package_data=True,

        install_requires=requirements, # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Programming Language :: Python :: 3",
        ]
)