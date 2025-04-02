from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    '''
    Input: 
        File path of requirements.txt

    Return:
        List of python packages to be installed
    '''
    requirements=[]
    with open(file_path) as f:
        requirements=f.readlines()
        output=[i for i in [req.replace("\n","") for req in requirements] if i != '-e .']
    
    return output


setup(
    name='mlproject-struct',
    version='3.12.0',
    author='mksgh',
    email='maniksingh099@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)