from enum import Enum
from pathlib import Path
import time

from shortwizard.editor_quizz import Quizz, QuizzList5Q

from shortwizard.ShortManager import ShortManager

from shortwizard.tts import tts
from shortwizard.tts import googletts

from shortwizard.file_manager import file_manager


class QuizzType(Enum):
    DYNAMIC5Q = 0
    COUPLE = 1
    LIST5Q = 2


def make_shorts_COUPLE(video_backgrounds_dir_path, quizzs_path, language, output_path):

    make_shorts(video_backgrounds_dir_path,
                quizzs_path, language, output_path, QuizzType.COUPLE)


def make_shorts_DYNAMIC5Q(video_backgrounds_dir_path, quizzs_path, language, output_path):

    make_shorts(video_backgrounds_dir_path,
                quizzs_path, language, output_path, QuizzType.DYNAMIC5Q)


def make_shorts_LIST5Q(video_backgrounds_dir_path, quizzs_path, language, output_path):

    make_shorts(video_backgrounds_dir_path,
                quizzs_path, language, output_path, QuizzType.LIST5Q)


def make_shorts(video_backgrounds_dir_path, quizzs_path, language, output_path, mode: QuizzType):

    match mode:
        # case QuizzType.DYNAMIC5Q:
        #     QuizzClass = QuizzDynamic5Q.QuizzDynamic5Q
        # case QuizzType.COUPLE:
        #     QuizzClass = QuizzCouple.QuizzCouple
        case QuizzType.LIST5Q:
            QuizzClass = QuizzList5Q.QuizzList5Q
        case _:
            raise ValueError("quizz_type error")

    sm: ShortManager = ShortManager(quizzs_path, QuizzClass)

    todays_date = time.strftime("%Y_%m_%d_%Hh%Mm%Ss")

    output_dir = file_manager.create_output_dir(
        output_path / f"JSON_{sm.get_group_name()}_IA_{language}_DATE_{todays_date}")

    # vbm = VideoBackgroundsManager.VideoBackgoundsManager(
    #     video_backgrounds_dir_path)

    while sm.has_next_short():

        match mode:
            case QuizzType.LIST5Q:
                quizz :QuizzList5Q.QuizzList5Q = sm.get_next_short()

        file_name = f"{quizz.get_number()}_{quizz.get_title()}"

        quizz.set_background_path(video_backgrounds_dir_path)

        quizz.create_sequence()

        quizz.get_sequence().render(output_dir / Path(file_name+".mp4"))

        # make_short(quizz, vbm, language, output_dir, mode)


# def make_short(quizz: Quizz.Quizz, vbm: VideoBackgroundsManager.VideoBackgoundsManager, language, output_path, mode: QuizzType):

#     temp_folder = file_manager.create_temp_folder()

#     googletts.generate_voices(quizz.get_tts_items(), language, temp_folder)

#     audio_clip, text_clip = editor.create_audio_and_text(
#         quizz.get_all_items(), create_text_clip_list_dynamic)

#     bg_video = editor.create_bg(vbm, audio_clip.duration+1.5)

#     file_name = f"{quizz.get_number()}_{quizz.get_title()}"

#     editor.write_final_render(
#         bg_video, text_clip, audio_clip, output_path, file_name)

#     file_manager.delete_folder(temp_folder)
