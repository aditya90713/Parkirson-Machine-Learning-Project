from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."


def get_requirement(file_path:str)->list[str]:
    '''
    this function will return list of requirements   
    
    '''
    requirements=[]
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [r.replace("\n", "") for r in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements





setup(

    name='parkisondisease',
    version='0.0.1',
    author='aditya gaikwad',
    author_email='aditya.gaikwad415@gmail.com',
    packages=find_packages(),
    install_requires=get_requirement('requirements.txt')

)