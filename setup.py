#The setup script is the center of all activity in building, distributing, and installing modules. 
#setup.py will also include information about the license.
from setuptools import setup,find_packages
from typing import List


PROJECT_NAME="housing-predictor"
VERSION="0.0.1"
AUTHOR="Ravi Teja Mandarapu"
DESCRIPTION="This is my End to End Machine Learning project with deployment"
#PACKAGES=["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"

#Declaring that all the values in list should be str format.
def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirements
    mention in the requirements.txt file

    return This function is going to return a list which contain name
    of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()

setup(

name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=find_packages(), #housing->function will install all the packages(folders) in the project which contains __init__.py
install_requires=get_requirements_list()   #for installing all the packages in requirements file

)