import tempfile
import os
from pathlib import Path
import shutil

root = Path(__file__).parent.parent


def create_temp_folder():
    """
    Create a temporary folder to store the files
    """
    temp_folder = tempfile.mkdtemp()
    return temp_folder


def create_output_dir(output_dir):
    """
    Create the output directory
    """
    full_path = Path(output_dir)
    if not os.path.exists(full_path):
        os.makedirs(full_path)
    return full_path


def delete_folder(folder):
    """
    Delete the folder
    """
    shutil.rmtree(folder)
