"""This module provides the shortwizard CLI."""
# rptodo/cli.py

from pathlib import Path
from typing import Optional

import typer

from shortwizard import ERRORS, __app_name__, __version__, config
from shortwizard import shortwizard

app = typer.Typer()


@app.command()
def init() -> None:
    """Initialize the shortwizard database."""
    app_init_error = config.init_app()
    if app_init_error:
        typer.secho(
            f'Creating config file failed with "{ERRORS[app_init_error]}"',
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)
    else:
        typer.secho(f"Init Ok", fg=typer.colors.GREEN)


@app.command()
def editclassic(
    video_backgrounds_dir_path: Path,
    audio_backgrounds_dir_path: Path,
    texts_path: Path,
    lang: str = typer.Option(default=None, help="IA language code."),
) -> None:
    typer.echo(
        f"Editing {video_backgrounds_dir_path}, {audio_backgrounds_dir_path}, {texts_path}, {lang}"
    )
    # shortwizard.edit_classic(
    #      video_backgrounds_dir_path, audio_backgrounds_dir_path, texts_path,Path.cwd(), lang
    #  )


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.command()
def editquizz(
    video_backgrounds_dir_path: Path,
    quizzs_path: Path,
    lang: str = typer.Option(default=None, help="IA language code."),
) -> None:
    typer.echo(
        f"Editing Quizzs {video_backgrounds_dir_path},{quizzs_path}, {lang}"
    )
    shortwizard.edit_quizz(
        video_backgrounds_dir_path, quizzs_path, Path.cwd(), lang
    )


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return
