import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "textSummarizer"
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/Configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",  # Corrected typo in "constants"
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Docker",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"  # Corrected the filename
]

for file_path in list_of_files:
    file_path = Path(file_path)
    file_dir, file_name = file_path.parent, file_path.name  # Use parent and name attributes

    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating Directory: {file_dir} for the file name {file_name}")

    if (not file_path.exists()) or (file_path.stat().st_size == 0):  # Use file_path.exists() and file_path.stat().st_size
        with open(file_path, 'w') as f:
            pass
            logging.info(f"Creating empty file: {file_path}")
    else:
        logging.info(f"{file_name} already exists")
