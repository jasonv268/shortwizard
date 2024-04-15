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
