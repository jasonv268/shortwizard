import time
from shortwizard.editor_quizz import QuizzsManager
from shortwizard.utils import file_manager, tts, editor, VideoBackgroundsManager, AudioBackgroundsManager


def make_shorts(video_backgrounds_dir_path, audio_backgrounds_dir_path, sound_effects_dir_path, quizzs_path, language, output_path):

    qm: QuizzsManager.QuizzsManager = QuizzsManager.QuizzsManager(quizzs_path)

    todays_date = time.strftime("%Y_%m_%d_%Hh%Mm%Ss")

    output_dir = file_manager.create_output_dir(
        output_path / f"JSON_{qm.get_group_name()}_IA_{language}_DATE_{todays_date}")

    vbm = VideoBackgroundsManager.VideoBackgoundsManager(
        video_backgrounds_dir_path)

    abm = AudioBackgroundsManager.AudioBackgroundsManager(
        audio_backgrounds_dir_path)

    while qm.has_next_quizz():

        quizz = qm.get_next_quizz()

        make_short(quizz, vbm, abm, language, output_dir)


def make_short(quizz: QuizzsManager.Quizz, vbm: VideoBackgroundsManager.VideoBackgoundsManager, abm: AudioBackgroundsManager.AudioBackgroundsManager, language, output_path):

    temp_folder = file_manager.create_temp_folder()

    tts.generate_voices(quizz.get_all_items(), language, temp_folder)

    audio_clip, text_clip = editor.create_audio_and_text(
        quizz.get_all_items(), abm)

    bg_video = editor.create_bg(vbm, audio_clip.duration+2)

    editor.write_final_render(
        bg_video, text_clip, audio_clip, output_path, quizz.get_title())

    file_manager.delete_folder(temp_folder)
