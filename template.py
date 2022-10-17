import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO, format='[%(asctime)s]--%(message)s')


package_name= 'DeepClassifier'

list_of_files= [
    '.github/workflows/.gitkeep',
    f'src/{package_name}/__init__.py',
    f'src/{package_name}/utils/__init__.py',
    f'src/{package_name}/config/__init__.py',
    f'src/{package_name}/entity/__init__.py',
    f'src/{package_name}/constants/__init__.py',
    f'src/{package_name}/components/__init__.py',
    f'src/{package_name}/pipeline/__init__.py',
    'configs/config.yaml',
    'dvc.yaml',
    'params.yaml',
    'init_setup.sh',
    'requirements.txt',
    'requirements_dev.txt',
    'setup.py',
    'setup.cfg',
    'pyproject.toml',
    'tox.ini',
    'research/trials.ipynb'
]

for filepath in list_of_files:
    try:
        filepath= Path(filepath)
        filedir, filename= os.path.split(filepath)
        if len(filedir)>=1:
            os.makedirs(filedir, exist_ok=True)
            msg= f'{filedir} created successfully for {filename}.'
            logging.info(msg)

        if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
            with open(filepath, 'w') as f:
                pass
                msg= f'{filename} created successfully.'
                logging.info(msg)
        else:
            msg= f"{filename} already exists."
            logging.info(msg)
    except Exception as e:
        raise e
    



