
import random

import moviepy.editor as mpe


from shortwizard.editor_utils.img.image import Image
from shortwizard.editor_utils.Sequence import Sequence

from shortwizard.config import root_assets
from shortwizard.editor_utils.img.Basique import Basique
from shortwizard.editor_utils.text import text_maker
from shortwizard.editor_utils.text.texte import Texte
from shortwizard.editor_utils.text.Basique import texte_grand_no_bg, texte_petit_white_bg_red
from shortwizard.editor_utils.video.VideoBackgroundsManager import VideoBackgroundsManager
from shortwizard.editor_utils.video import video_maker, video_utils
from shortwizard.editor_utils.video.Video import Video

from shortwizard.editor_utils.audio.audio import Audio, basique

from shortwizard.editor_utils.img import animation, image_utils

from shortwizard.editor_utils import colors


class Background(Sequence):
    def __init__(self, start_time, duration, video_background_path) -> None:
        super().__init__(start_time, duration)

        vbm = VideoBackgroundsManager(video_background_path)

        background = video_maker.create_bg(vbm, duration)

        self.objects += [background]


class Chrono(Sequence):
    def __init__(self):
        super().__init__(0)

        chrono = Image(root_assets / "image" / "chrono.png",
                       ("center", 400), Basique(zoom=2), animation.battement)

        volume_reduction = basique.Basique(volume=0.1)

        sound = Audio(root_assets / "audio_effects" / "clock.mp3",
                      basique=volume_reduction)

        self.objects = [chrono, sound]


class Annonce(Sequence):
    def __init__(self, text_content, emote_name, tts):
        super().__init__(0)

        annonce = Texte(text_content, ("center", 500),
                        texte_grand_no_bg, tts, animation=True)

        self.duration = annonce.duration-0.3

        emote_resize = Basique(mask_color=(4, 253, 45), zoom=0.4)

        emote = Video(root_assets / "video" / f"{emote_name}.mp4",
                      ("center", 220), basique=emote_resize, animation=animation.slide).set_start(0).set_end(annonce.duration-0.3)

        self.objects = [emote, annonce]


class Question(Sequence):
    def __init__(self, text_content, tts):
        super().__init__(0)

        question = Texte(text_content, ("center", 500),
                         texte_grand_no_bg, tts, animation=True).set_start(0)

        swoosh = mpe.AudioFileClip(root_assets /
                                   "audio_effects" / "swoosh.mp3").set_start(-0.2)

        chrono = Chrono().set_start(question.duration).set_end(question.duration-0.3+3)

        emote_resize = Basique(mask_color=(4, 253, 45), zoom=0.4)

        emotes = ["ne_sait_pas_homme", "ne_sait_pas_femme", "bizzare"]

        emote = Video(root_assets / "video" / f"{random.choice(emotes)}.mp4",
                      ("center", 270), basique=emote_resize, animation=animation.slide).set_start(0).set_end(question.duration-0.3)

        self.duration = question.duration-0.3+3

        self.objects = [swoosh, emote, question, chrono]


class Reponse(Sequence):
    def __init__(self, text_content, position, tts):
        super().__init__(0)

        reponse = Texte(text_content, ("center", 500),
                        texte_grand_no_bg, tts, animation=True)

        reponse2 = Texte(text_content, position, texte_petit_white_bg_red.set_background_color(
            None, copy=True)).set_start(reponse.duration)

        self.duration = reponse.duration-0.3+1

        self.objects = [reponse, reponse2]
