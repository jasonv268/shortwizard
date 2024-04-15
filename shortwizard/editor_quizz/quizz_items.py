from math import sin
from math import radians
import random
import time
from pathlib import Path
import moviepy.editor as mpe

from shortwizard.editor_utils.Sequence import Sequence
from shortwizard.tts import tts
from shortwizard.file_manager import file_manager

from shortwizard.editor_utils.audio import tts_maker

from shortwizard.config import root_assets
from shortwizard.editor_utils.text import text_maker

from shortwizard.editor_utils.video.VideoBackgroundsManager import VideoBackgroundsManager
from shortwizard.editor_utils.video import video_maker, video_utils

from shortwizard.editor_utils import colors


class Title(Sequence):
    def __init__(self, text_content, start_time):
        super().__init__(start_time)

        tts_title = tts_maker.create_tts(text_content, "fr", tts_maker.Mode.GOOGLE_LOW).set_start(start_time)
        title = text_maker.create_text_clip_list_dynamic(text_content.upper(), ("center", 400), start_time, start_time+tts_title.duration, 70, 20)

        self.duration = tts_title.duration

        self.objects += [*title, tts_title]


class Background(Sequence):
    def __init__(self, start_time, duration, video_background_path) -> None:
        super().__init__(start_time, duration)

        vbm = VideoBackgroundsManager(video_background_path)

        background = video_maker.create_bg(vbm, duration)

        self.objects += [background]


class Annonce(Sequence):

    def __init__(self, text_content, start_time) -> None:
        super().__init__(start_time)

        tts_annonce = tts_maker.create_tts(text_content, "fr", tts_maker.Mode.GOOGLE_LOW).set_start(start_time)
        annonce = text_maker.create_text_clip_list_dynamic(text_content.upper(), ("center", 400), start_time, start_time+tts_annonce.duration, 70, 20)

        self.duration = tts_annonce.duration

        self.objects += [*annonce, tts_annonce]


class Questions(Sequence):
    def __init__(self, start_time) -> None:
        super().__init__(start_time)

        y_anchor_position = 850

        self.objects = [text_maker.create_text2(start_time,"FACILE", 70, 25, (50, y_anchor_position), background_color=colors.GREEN),
                        text_maker.create_text(start_time,"1)", (50, y_anchor_position+100), "white", 70,25),
                        text_maker.create_text(start_time,"2)", (50, y_anchor_position+200), "white", 70,25),
                        text_maker.create_text2(start_time,"MOYEN", 70, 25, (50, y_anchor_position+300), background_color=colors.ORANGE),
                        text_maker.create_text(start_time,"3)", (50, y_anchor_position+400), "white", 70,25),
                        text_maker.create_text(start_time,"4)", (50, y_anchor_position+500), "white", 70,25),
                        text_maker.create_text2(start_time,"DIFFICILE", 70, 25, (50, y_anchor_position+600), background_color=colors.RED),
                        text_maker.create_text(start_time,"5)", (50, y_anchor_position+700), "white", 70,25)]

        self.duration = 0

        self.t = start_time

        self.reponse_position = (120, y_anchor_position+100)

class Effet(Sequence):
    def __init__(self, start_time, duration):
        super().__init__(start_time)

        effet = mpe.VideoFileClip(root_assets / "video" / "ne_sait_pas_femme.mp4").set_start(start_time).set_position(("center", 250))
        if effet.duration > duration:
            effet = effet.set_duration(duration)

        effet = effet.resize(0.4)

        effet = video_utils.remove_green_screen(effet,(4, 253, 45))

        self.objects = [effet]

class Chrono(Sequence):
    def __init__(self, start_time, duration):
        super().__init__(start_time)

        chrono = mpe.ImageClip(root_assets / "image" / "chrono.png").set_start(start_time).set_position(("center", 300)).set_duration(duration)

        chrono = chrono.resize(2)

        speed_coefficient = 5

        chrono = chrono.resize(lambda t: (chrono.w * (1 + sin(speed_coefficient * t) * 0.2), chrono.h * (1 + sin(speed_coefficient * t) * 0.2)))

        sound = mpe.AudioFileClip(root_assets / "audio_effects" / "clock.mp3").set_start(start_time).set_duration(duration)

        self.duration = duration

        self.objects = [chrono, sound]

class Question(Sequence):
    def __init__(self, text_content, start_time):
        super().__init__(start_time)


        tts_question= tts_maker.create_tts(text_content.upper(), "fr", tts_maker.Mode.GOOGLE_LOW).set_start(start_time)

        question = text_maker.create_text_clip_list_dynamic(
            text_content, ("center", 500), start_time, start_time+tts_question.duration, 70, 20)

        swoosh = mpe.AudioFileClip(root_assets /
                                "audio_effects" / "swoosh.mp3").set_start(start_time-0.2)

        chrono = Chrono(start_time+ tts_question.duration, 3)

        effet = Effet(start_time, tts_question.duration)
        
        self.duration = tts_question.duration+3

        self.objects = [swoosh, effet, *question, tts_question, chrono]


class Reponse(Sequence):
    def __init__(self, text_content, start_time, position):
        super().__init__(start_time)

        tts_reponse = tts_maker.create_tts(text_content.upper(), "fr", tts_maker.Mode.GOOGLE_LOW).set_start(start_time)

        reponse = text_maker.create_text_clip_list_dynamic(
            text_content, ("center", 500), start_time, start_time+tts_reponse.duration, 70, 25)

        reponse2 = mpe.TextClip(text_content, fontsize=70, color='white', stroke_color='black',
                                stroke_width=2, font='Tiktok').set_start(start_time+1).set_position(position)

        self.duration = tts_reponse.duration+1

        self.objects = [*reponse, reponse2, tts_reponse]
    
