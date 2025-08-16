# used to build our application as a package that could be installed via pip 
# (build script and configuration for your package)

from setuptools import find_packages , setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(filePath:str)->List[str]:
    # will return the list requirements
    requirements = List[str]
    with open(filePath) as file_obj:
        requirements= file_obj.readlines()
        requirements= [ req.replace('\n' , '') for req in requirements]
        if HYPEN_E_DOT in requirements: 
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name= 'first_project',
    version='0.0.1',
    author='elgho',
    packages=find_packages(), # it will look to the folders that contains __init__.py
    # as it will contain the imported packages and so
    install_requires=get_requirements('requirements.txt') # the needed packages to be installed

)