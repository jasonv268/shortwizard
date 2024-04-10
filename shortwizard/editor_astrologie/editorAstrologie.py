import time

from shortwizard.editor_astrologie.Astrologie import Astrologie
from shortwizard.ShortManager import ShortManager

from shortwizard.editor_utils import editor
from shortwizard.editor_utils.video import VideoBackgroundsManager
from shortwizard.editor_utils.text.text_utils import create_text_clip_list, create_text_clip_list_dynamic

from shortwizard.tts import tts

from shortwizard.file_manager import file_manager


def make_shorts_ASTRO(video_backgrounds_dir_path, astros_path, language, output_path):

    make_shorts(video_backgrounds_dir_path,
                astros_path, language, output_path)


def make_shorts(video_backgrounds_dir_path, quizzs_path, language, output_path):
    sm: ShortManager = ShortManager(quizzs_path, Astrologie)

    todays_date = time.strftime("%Y_%m_%d_%Hh%Mm%Ss")

    output_dir = file_manager.create_output_dir(
        output_path / f"JSON_{sm.get_group_name()}_IA_{language}_DATE_{todays_date}")

    vbm = VideoBackgroundsManager.VideoBackgoundsManager(
        video_backgrounds_dir_path)

    while sm.has_next_short():

        quizz = sm.get_next_short()

        make_short(quizz, vbm, language, output_dir)


def make_short(quizz: Astrologie, vbm: VideoBackgroundsManager.VideoBackgoundsManager, language, output_path):

    temp_folder = file_manager.create_temp_folder()

    tts.generate_voices(quizz.get_all_items(), language, temp_folder)

    audio_clip, text_clip = editor.create_audio_and_text(
        quizz.get_all_items(), create_text_clip_list_dynamic)

    bg_video = editor.create_bg(vbm, audio_clip.duration+1.5)

    file_name = f"{quizz.get_number()}_{quizz.get_title()}"

    editor.write_final_render(
        bg_video, text_clip, audio_clip, output_path, file_name)

    file_manager.delete_folder(temp_folder)
