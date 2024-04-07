import time
from shortwizard.editor_quizz import QuizzsManager
from shortwizard.utils import file_manager, tts, editor, VideoBackgroundsManager, AudioBackgroundsManager

from shortwizard.editor_quizz.editorQuizz_assets import create_text_clip_list, create_text_clip_list_dynamic


def make_shorts(video_backgrounds_dir_path, quizzs_path, language, output_path):

    qm: QuizzsManager.QuizzsManager = QuizzsManager.QuizzsManager(quizzs_path)

    todays_date = time.strftime("%Y_%m_%d_%Hh%Mm%Ss")

    output_dir = file_manager.create_output_dir(
        output_path / f"JSON_{qm.get_group_name()}_IA_{language}_DATE_{todays_date}")

    vbm = VideoBackgroundsManager.VideoBackgoundsManager(
        video_backgrounds_dir_path)

    while qm.has_next_quizz():

        quizz = qm.get_next_quizz()

        make_short(quizz, vbm, language, output_dir)


def make_short(quizz: QuizzsManager.Quizz, vbm: VideoBackgroundsManager.VideoBackgoundsManager, language, output_path):

    temp_folder = file_manager.create_temp_folder()

    tts.generate_voices(quizz.get_all_items(), language, temp_folder)

    audio_clip, text_clip = editor.create_audio_and_text(
        quizz.get_all_items(), create_text_clip_list_dynamic)

    bg_video = editor.create_bg(vbm, audio_clip.duration+1.5)

    file_name = f"{quizz.get_number()}_{quizz.get_title()}"

    editor.write_final_render(
        bg_video, text_clip, audio_clip, output_path, file_name)

    file_manager.delete_folder(temp_folder)
