"""This module provides the RP To-Do config functionality."""
# rptodo/config.py

import configparser
from pathlib import Path

import typer

from shortwizard import (
    DIR_ERROR, FILE_ERROR, SUCCESS, __app_name__
)


root = Path(__file__).parent.parent

root_assets = root / "shortwizard" / "assets"

CONFIG_DIR_PATH = Path(typer.get_app_dir(__app_name__))
CONFIG_FILE_PATH = CONFIG_DIR_PATH / "config.ini"


def init_app() -> int:
    """Initialize the application."""
    config_code = _init_config_file()
    if config_code != SUCCESS:
        return config_code

    config_emotes = _init_emotes_shortcuts()
    if config_emotes != SUCCESS:
        return config_emotes
    return SUCCESS


def _init_config_file() -> int:
    try:
        CONFIG_DIR_PATH.mkdir(exist_ok=True)
    except OSError:
        return DIR_ERROR
    try:
        CONFIG_FILE_PATH.touch(exist_ok=True)
    except OSError:
        return FILE_ERROR
    return SUCCESS


def _init_emotes_shortcuts() -> int:
    try:
        emotes_dir = root_assets / "video" / "emotes" / "pack1"
        # Utiliser une clé de tri insensible à la casse pour trier les noms de fichiers

        emotes_list = [(int(file.name.split("_")[0]), file.name.split("_")[1])
                       for file in emotes_dir.iterdir() if file.is_file()]
        emotes_list.sort(key=lambda x: x[0])

        python_file = "from pathlib import Path\nfrom shortwizard.config import root_assets\nfrom shortwizard.editor_utils.video.Video import Video\nfrom shortwizard.editor_utils.img.Basique import default_has_mask\n\n"

        python_file+="def get_emote(number)->Video:\n\treturn Video(globals()[f'_{number}'],basique=default_has_mask)\n\n"

        for (id, name) in emotes_list:
            python_file += f"_{id}_{name.split(".")[0].replace(" ", "_").replace(
                "-", "_")} = Path(root_assets /'video' / 'emotes' / 'pack1' / '{id}_{name}')\n"
            python_file += f"_{id}=_{id}_{name.split(
                ".")[0].replace(" ", "_").replace("-", "_")}\n"

        with open(root / "shortwizard" / "editor_utils" / "emotes.py", "w") as file:
            file.write(python_file)

    except OSError:
        return FILE_ERROR
    return SUCCESS
