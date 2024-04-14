import random
import time
from pathlib import Path
import moviepy.editor as mpe

from shortwizard.editor_utils.Sequence import Sequence
from shortwizard.tts import tts
from shortwizard.file_manager import file_manager

from shortwizard.config import root
from shortwizard.editor_utils.video.video_utils import crop_bg
from shortwizard.editor_utils.text.text_utils import create_text_clip_list_dynamic


# class Title(Sequence):
#     def __init__(self, text_content, start_time):
#         super().__init__()
#         self.text_content = text_content

#         title = mpe.TextClip(text_content, fontsize=90, color='red', stroke_color='black',
#                              stroke_width=5, font='Tiktok-Bold').set_start(start_time).set_duration(2).set_position(("center", "center"))

#         self.objects += [title]


class Background(Sequence):
    def __init__(self, start_time, duration) -> None:
        super().__init__(start_time, duration)

        background = mpe.VideoFileClip(
            root / "bgvid" / "7249-199191048.mp4").set_duration(duration)
        background = crop_bg(background)

        self.objects += [background]


class Questions(Sequence):
    def __init__(self, start_time) -> None:
        super().__init__(start_time)

        self.objects = []

        self.reponse_position = (50, 500)

    def add_question(self, text_content, start_time):

        self.objects += question(text_content, start_time)

    def add_reponse(self, text_content, start_time):

        self.objects += reponse(text_content, start_time,
                                self.reponse_position)
        self.reponse_position = (
            self.reponse_position[0], self.reponse_position[1]+100)


def title(text_content, start_time):
    title = mpe.TextClip(text_content, fontsize=90, color='red', stroke_color='black',
                         stroke_width=5, font='Tiktok-Bold').set_start(start_time).set_duration(2).set_position(("center", "center"))

    return [title]


def background(duration):
    background = mpe.VideoFileClip(
        root / "bgvid" / "7249-199191048.mp4").set_duration(duration)
    background = crop_bg(background)

    return [background]


def question(text_content, start_time):

    temp_path = file_manager.create_temp_folder() / Path("temp.mp3")

    tts.generate_voice(text_content, temp_path)
    time.sleep(1)

    tts_question = mpe.AudioFileClip(temp_path).set_start(start_time)

    file_manager.delete_folder(temp_path.parent)

    question = create_text_clip_list_dynamic(
        text_content, ("center", 200), start_time, start_time+tts_question.duration, 70, 25)

    swoosh = mpe.AudioFileClip(root / "shortwizard"/"assets" /
                               "audio_effects" / "swoosh.mp3").set_start(start_time-0.5)

    chrono = mpe.VideoFileClip(root / "shortwizard" / "assets" / "video" /
                               "chrono.mp4").set_start(start_time+tts_question.duration)

    return [swoosh, *question, tts_question]


def reponse(text_content, start_time, position):
    reponse = mpe.TextClip(text_content, fontsize=90, color='red', stroke_color='black',
                           stroke_width=5, font='Tiktok-Bold').set_start(start_time).set_duration(2).set_position(("center", 200))

    reponse2 = mpe.TextClip(text_content, fontsize=90, color='red', stroke_color='black',
                            stroke_width=5, font='Tiktok-Bold').set_start(start_time+1).set_position(position)

    return [reponse, reponse2]
