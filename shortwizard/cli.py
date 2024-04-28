"""This module provides the shortwizard CLI."""
# rptodo/cli.py

from pathlib import Path
from typing import Optional

import typer

from shortwizard import ERRORS, __app_name__, __version__, config
from shortwizard.editor_quizz import editorQuizz


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
def edit_quiz_list5q(
    video_backgrounds_dir_path: Path,
    quizzs_path: Path,
    lang: str = typer.Option(default="fr-fr", help="IA language code."),
    ia: str = typer.Option(default="google-low", help="IA name."),
) -> None:
    typer.echo(
        f"Editing Quizzs Couple{video_backgrounds_dir_path},{quizzs_path}, {ia},{lang}"
    )
    editorQuizz.make_shorts_LIST5Q(video_backgrounds_dir_path,
                                   quizzs_path, ia ,lang, Path.cwd())
    

@app.command()
def edit_quiz_choice5q(
    video_backgrounds_dir_path: Path,
    quizzs_path: Path,
    lang: str = typer.Option(default="fr-fr", help="IA language code."),
    ia: str = typer.Option(default="google-low", help="IA name."),
) -> None:
    typer.echo(
        f"Editing Quizzs Couple{video_backgrounds_dir_path},{quizzs_path}, {ia},{lang}"
    )
    editorQuizz.make_shorts_CHOICE5Q(video_backgrounds_dir_path,
                                   quizzs_path, ia ,lang, Path.cwd())


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
