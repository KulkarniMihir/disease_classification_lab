import os
from pathlib import Path
import logging

#Log current time & message
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(messsage)s:')

project_name = 'cnn_classifier'

list_of_files = [
    "./github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py", #package constructer file
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/experiments.ipynb",
    "templates/index.html"
]

for file_path in list_of_files:
    # setup path
    file_path = Path(file_path)
    filedir, filename = os.path.split(file_path)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, "w") as f:
            pass
            logging.info(f"Creating empty file: {file_path}")

    else:
        logging.info(f"{filename} alrady exists")                
