from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
#my function will return a list(a list of requirements) so it is written as:
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    #to open requirements.txt
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()  #requirements.txt will be read
        requirements=[req.replace("\n","")for req in requirements]  #replace \n with blank
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements    



#meta data 
setup(
    name='machinelearningproject',
    version='0.0.1',
    author='Ritwika',
    author_email='ritwikaghosh2003@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)