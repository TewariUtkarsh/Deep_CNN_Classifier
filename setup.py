import setuptools
from typing import List

readme_filepath= r'README.md'
__version__= '0.0.1'
REPO_NAME= 'Deep_CNN_Classifier'
AUTHOR_NAME= 'TewariUtkarsh'
AUTHOR_EMAIL= 'tewariutkarsh@outlook.com'
SRC_NAME= 'DeepClassifier'
REQUIREMENT_FILEPATH= r'requirements.txt'
with open(readme_filepath, 'r') as file_obj:
    long_description= file_obj.read()


def get_requirements_packages(filepath:str) -> List[str]:
    with open(REQUIREMENT_FILEPATH, 'r') as file_obj:
        packages=[]
        for p in file_obj.readlines():
            if p!='' and p!='-e .':
                packages.append(p[:-1])
    return packages

setuptools.setup(
    name= SRC_NAME,
    version=__version__,
    description='A basic python package',
    long_description=long_description,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    url= f'https://github.com/{AUTHOR_NAME}/{REPO_NAME}',
    project_urls= {
        'Bugs': f'https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues'
    },
    install_requires=get_requirements_packages(filepath=REQUIREMENT_FILEPATH),
    package_dir={"": "src"},
    packages=setuptools.find_packages(where='src')
)

