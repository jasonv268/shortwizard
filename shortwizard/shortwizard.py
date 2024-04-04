"""This module provides the RP To-Do model-controller."""
# rptodo/rptodo.py

from pathlib import Path
# from shortwizard.editors import editorClassic
from shortwizard.editor_quizz import editorQuizz



def edit_classic(video_backgrounds_dir_path: Path, audio_backgrounds_dir_path: Path, texts_path: Path, output_path: Path, lang: str,) -> None:
    # editorClassic.make_shorts(video_backgrounds_dir_path,
    #                           audio_backgrounds_dir_path, texts_path, output_path, lang)
    pass


def edit_quizz(video_backgrounds_dir_path: Path, quizzs_path: Path, output_path: Path, lang: str,) -> None:
    editorQuizz.make_shorts(video_backgrounds_dir_path, quizzs_path,lang, output_path)
    