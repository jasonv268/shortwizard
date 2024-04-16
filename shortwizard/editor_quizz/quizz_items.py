
import random

import moviepy.editor as mpe


from shortwizard.editor_utils.img.image import Image
from shortwizard.editor_utils.Sequence import Sequence
from shortwizard.editor_utils.audio import Tts

from shortwizard.config import root_assets
from shortwizard.editor_utils.img.Basique import Basique
from shortwizard.editor_utils.text import text_maker
from shortwizard.editor_utils.text.texte import Texte
from shortwizard.editor_utils.text.Basique import texte_grand_no_bg, texte_petit_white_bg_red
from shortwizard.editor_utils.video.VideoBackgroundsManager import VideoBackgroundsManager
from shortwizard.editor_utils.video import video_maker, video_utils
from shortwizard.editor_utils.video.Video import Video

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
                       ("center", 300), Basique(zoom=2), animation.battement).render()

        sound = mpe.AudioFileClip(root_assets / "audio_effects" /
                                  "clock.mp3").set_start(0)

        self.objects = [chrono, sound]


class Annonce(Sequence):
    def __init__(self, text_content, emote_name):
        super().__init__(0)

        tts = Tts.Tts("fr", Tts.Mode.GOOGLE_LOW)

        annonce = Texte(text_content.upper(), ("center", 500),
                        texte_grand_no_bg, tts, animation=True).render()

        self.duration = annonce.duration

        emote_resize = Basique(mask_color=(4, 253, 45), zoom=0.4)

        emote = Video(root_assets / "video" / f"{emote_name}.mp4",
                       ("center", 220), basique=emote_resize, animation=animation.slide).render()
        emote.start_at(0).stop_at(annonce.duration)

        self.objects = [emote, annonce]


class Question(Sequence):
    def __init__(self, text_content):
        super().__init__(0)

        tts = Tts.Tts("fr", Tts.Mode.GOOGLE_LOW)

        question = Texte(text_content.upper(), ("center", 500),
                         texte_grand_no_bg, tts, animation=True).render().start_at(0)

        swoosh = mpe.AudioFileClip(root_assets /
                                   "audio_effects" / "swoosh.mp3").set_start(-0.2)

        chrono = Chrono().start_at(question.duration).stop_at(question.duration+3)

        emote_resize = Basique(mask_color=(4, 253, 45), zoom=0.4)

        emotes = ["ne_sait_pas_homme", "ne_sait_pas_femme", "bizzare"]

        emote = Video(root_assets / "video" / f"{random.choice(emotes)}.mp4",
                       ("center", 250), basique=emote_resize, animation=animation.slide).render()
        emote.start_at(0).stop_at(question.duration)

        self.duration = question.duration+3

        self.objects = [swoosh, emote, question, chrono]


class Reponse(Sequence):
    def __init__(self, text_content, position):
        super().__init__(0)

        tts = Tts.Tts("fr", Tts.Mode.GOOGLE_LOW)

        reponse = Texte(text_content.upper(), ("center", 500),
                        texte_grand_no_bg, tts, animation=True).render()

        reponse2 = Texte(text_content, position, texte_petit_white_bg_red.set_background_color(None, copy=True)).render(
        ).start_at(reponse.duration)

        self.duration = reponse.duration+1

        self.objects = [reponse, reponse2]
