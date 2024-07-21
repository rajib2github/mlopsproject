from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_prereuisites(file_path:str)->List[str]:
    prerequisites= []

    with open(file_path) as file_obj:
        prerequisites = file_obj.readline()
        prerequisites= (preq.replace("\n","") for preq in prerequisites)
    if HYPEN_E_DOT in prerequisites:
        prerequisites.remove(HYPEN_E_DOT)

    return prerequisites

setup(
    name="mlproject",
    version="0.0.1",
    author="rajib",
    packages=find_packages(),
    install_requires=get_prereuisites('prerequisites.txt')

)