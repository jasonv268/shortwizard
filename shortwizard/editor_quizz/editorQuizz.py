from enum import Enum
from pathlib import Path
import time

from shortwizard.editor_quizz import QuizzList5Q

from shortwizard.ShortManager import ShortManager

from shortwizard.tts import tts

from shortwizard.file_manager import file_manager


class QuizzType(Enum):
    DYNAMIC5Q = 0
    COUPLE = 1
    LIST5Q = 2


def make_shorts_LIST5Q(video_backgrounds_dir_path, quizzs_path, ia, language, output_path):

    make_shorts(video_backgrounds_dir_path,
                quizzs_path, ia ,language, output_path,  QuizzType.LIST5Q)


def make_shorts(video_backgrounds_dir_path, quizzs_path, ia, language, output_path, mode: QuizzType):

    tts_mode = None
    ia_tts = None

    match ia:
        case "google-low":
            tts_mode = tts.Mode.GOOGLE_LOW
        case "google-high":
            tts_mode = tts.Mode.GOOGLE_HIGH
        case "watson":
            tts_mode = tts.Mode.WATSON

    match language:
        case "fr-fr":
            ia_tts = tts.Tts("fr", tts_mode)
        case "en-en":
            ia_tts = tts.Tts("en", tts_mode)

    match mode:
        case QuizzType.LIST5Q:
            QuizzClass = QuizzList5Q.QuizzList5Q
        case _:
            raise ValueError("quizz_type error")

    sm: ShortManager = ShortManager(quizzs_path, QuizzClass)

    todays_date = time.strftime("%Y_%m_%d_%Hh%Mm%Ss")

    output_dir = file_manager.create_output_dir(
        output_path / f"DATE_{todays_date}_JSON_{sm.get_group_name()}_IA_{ia}_LANG_{language}")

    while sm.has_next_short():

        match mode:
            case QuizzType.LIST5Q:
                quizz :QuizzList5Q.QuizzList5Q = sm.get_next_short()

        file_name = f"{quizz.get_number()}_{quizz.get_title()}"

        quizz.set_background_path(video_backgrounds_dir_path)

        quizz.set_ia_tts(ia_tts)

        quizz.create_sequence()

        quizz.get_sequence().render(output_dir / Path(file_name+".mp4"))

        quizz.get_sequence().close()
