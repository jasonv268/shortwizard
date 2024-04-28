
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

from shortwizard.editor_utils import colors, emotes

from shortwizard.editor_utils.VideoSequence import VideoSequence


class Background(Sequence):
    def __init__(self, start, duration, video_background_path) -> None:
        super().__init__(start)

        vbm = VideoBackgroundsManager(video_background_path)

        background = video_maker.create_bg(vbm, duration)

        self.objects += [background]

        self.duration = duration


class Chrono(Sequence):
    def __init__(self):
        super().__init__(0)

        # chrono = Image(root_assets / "image" / "chrono.png",
        #                ("center", 400), Basique(resize=2), animation.battement)

        volume_reduction = basique.Basique(volume=0.1)

        sound = Audio(root_assets / "audio_effects" / "clock.mp3",
                      basique=volume_reduction)

        self.objects = [sound]


class Annonce(Sequence):
    def __init__(self, text_content, emote_liste, tts):
        super().__init__(0)

        annonce = Texte(text_content, ("center", 500),
                        (750, 1920), texte_grand_no_bg, tts, animation=True)

        self.duration = annonce.duration-0.3

        emote_num = random.choice(emote_liste)

        emote: VideoSequence = emotes.get_emote(emote_num).set_start(0).set_end(
            annonce.duration-0.3).basique.set_resize(0.4)
        emote.set_position((400, 280)).set_animation(animation.slide)

        self.objects = [emote, annonce]


class Question(Sequence):
    def __init__(self, text_content, tts):
        super().__init__(0)

        question = Texte(text_content, ("center", 500), (750, 1920),
                         texte_grand_no_bg, tts, animation=True).set_start(0)

        swoosh = mpe.AudioFileClip(root_assets /
                                   "audio_effects" / "swoosh.mp3").set_start(-0.2)

        chrono = Chrono().set_start(question.duration).set_end(question.duration-0.3+3)

        emote_num = random.choice([127, 126, 22, 83])

        emote: VideoSequence = emotes.get_emote(emote_num).set_start(0).set_end(
            question.duration).basique.set_resize(0.4).set_position((400, 280)).set_animation(animation.slide)

        self.duration = question.duration-0.3+3

        self.objects = [swoosh, emote, question, chrono]


class QuestionChoice(Sequence):
    def __init__(self, question, reponse_valide, choix, tts):
        super().__init__(0)

        question = Texte(question, ("center", 500), (750, 1920),
                         texte_grand_no_bg, tts, animation=True).set_start(0)

        swoosh = mpe.AudioFileClip(root_assets /
                                   "audio_effects" / "swoosh.mp3").set_start(-0.2)

        volume_reduction = basique.Basique(volume=0.1)

        sound = Audio(root_assets / "audio_effects" / "clock.mp3",
                      basique=volume_reduction)

        chrono = sound.set_start(question.duration).set_end(
            question.duration-0.3+3)

        emote_num = random.choice([127, 126, 22, 83])

        emote: VideoSequence = emotes.get_emote(emote_num).set_start(0).set_end(
            question.duration).basique.set_resize(0.4).set_position((400, 280)).set_animation(animation.slide)

        rand = random.randint(0, 1)

        if rand == 0:

            choix1 = Texte(reponse_valide, ("center", 400), (2000, 1920),
                           texte_petit_white_bg_red.set_background_color(colors.ORANGE, copy=True)).set_start(question.duration).set_end(question.duration-0.3+5)

            ou = Texte("ou", ("center", 500), (2000, 1920), texte_petit_white_bg_red.set_background_color(
                colors.BLUE, copy=True)).set_start(question.duration).set_end(question.duration-0.3+5)

            choix2 = Texte(choix, ("center", 600), (2000, 1920),
                           texte_petit_white_bg_red.set_background_color(colors.RED, copy=True)).set_start(0).set_start(question.duration).set_end(question.duration-0.3+5)

            choix_valide = Texte(reponse_valide, ("center", 400), (2000, 1920),
                                 texte_petit_white_bg_red.set_background_color(colors.GREEN, copy=True)).set_start(question.duration-0.3+3).set_end(question.duration-0.3+5)

        else:
            choix1 = Texte(choix, ("center", 400), (2000, 1920),
                           texte_petit_white_bg_red.set_background_color(colors.ORANGE, copy=True)).set_start(question.duration).set_end(question.duration-0.3+5)

            ou = Texte("ou", ("center", 500), (2000, 1920), texte_petit_white_bg_red.set_background_color(
                colors.BLUE, copy=True)).set_start(question.duration).set_end(question.duration-0.3+5)

            choix2 = Texte(reponse_valide, ("center", 600), (2000, 1920),
                           texte_petit_white_bg_red.set_background_color(colors.RED, copy=True)).set_start(0).set_start(question.duration).set_end(question.duration-0.3+5)

            choix_valide = Texte(reponse_valide, ("center", 2000), (900, 1920),
                                 texte_petit_white_bg_red.set_background_color(colors.GREEN, copy=True)).set_start(question.duration-0.3+3).set_end(question.duration-0.3+5)

        self.objects = [swoosh, emote, question,
                        chrono, choix1, ou, choix2, choix_valide]

        self.duration = question.duration-0.3+5


class ReponseChoice(Sequence):
    def __init__(self, text_content, position, tts) -> None:
        pass


class Reponse(Sequence):
    def __init__(self, text_content, position, tts):
        super().__init__(0)

        reponse = Texte(text_content, ("center", 500), (750, 1920),
                        texte_grand_no_bg, tts, animation=True)

        reponse2 = Texte(text_content,  position, (900 - position[0], 1920), texte_petit_white_bg_red.set_background_color(
            None, copy=True)).set_start(reponse.duration)

        self.duration = reponse.duration-0.3+1

        self.objects = [reponse, reponse2]
