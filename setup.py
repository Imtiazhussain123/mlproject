## to find all packages from enviroment and set  for doing all setups

from setuptools import find_packages, setup 
from typing import List

HYPEN_E_DOT = "-e ."
def get_requirements(fiel_path:str)-> List[str]:
    ''''
        This function will return the list of requirements library from requirement.txt

    '''
    requirements =[]
    with open(fiel_path) as file_obj:
        requirements = file_obj.readlines() 
        requirements = [req.replace("\n"," ")for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

        return requirements
##setup for required packages, libraries, author nad version,
setup(

    name= 'mlproject',
    version= '0.0.1',
    author= 'Imtiaz',
    author_email= 'imtiazh183@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt'),
)
