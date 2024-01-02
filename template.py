import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

projectname = "mlops_pipeline"

list_of_file = [
    ".github/workflows/.gitkeep",
    f"src/{projectname}/__init__.py",
    f"src/{projectname}/components/__init__.py",
    f"src/{projectname}/components/data_ingestion.py",
    f"src/{projectname}/components/data_transformation.py",
    f"src/{projectname}/pipelines/__init__.py",
    f"src/{projectname}/pipelines/training_pipeline.py",
    f"src/{projectname}/pipelines/prediction_pipeline.py",
    f"src/{projectname}/logger.py",
    f"src/{projectname}/exception.py",
    f"src/{projectname}/utils.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"
]

for filepath in list_of_file:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating Directory: {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")