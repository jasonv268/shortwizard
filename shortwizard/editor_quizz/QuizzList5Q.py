from shortwizard.editor_quizz.Quizz import Quizz

from shortwizard.editor_utils.Sequence import Sequence

from shortwizard.editor_quizz.quizz_items import *

from shortwizard.editor_utils.text.texte import Texte
from shortwizard.editor_utils.text.Basique import texte_petit_black_bg_white, texte_petit_white_bg_red

from shortwizard.editor_utils import colors

from shortwizard.text_generator.text_generator import get_random_food
import random





class QuizzList5Q(Quizz):

    def __init__(self, json_quizz, number):
        super().__init__(json_quizz, number)

    def set_background_path(self, path):
        self.video_background_path = path

    def set_ia_tts(self, ia_tts):
        self.ia_tts = ia_tts

    def create_sequence(self):
        t = 0

        anchor_tag = Texte(
            "@quizz_pour_tous", ("center", 1700), texte_petit_black_bg_white).render().start_at(0)

        anchor_title = Texte(
            self.json_quizz["titre"], ("center", 100), texte_petit_white_bg_red.set_font_size(80,copy=True)).render().start_at(t)
        
        self.sequence.objects += [anchor_tag, anchor_title]

        sequence_questions = Sequence(t)
        self.sequence.objects += [sequence_questions]

        y_anchor_position = 850

        anchor_infos = Sequence(t)
        anchor_infos.objects += [Texte("FACILE", (100, y_anchor_position), texte_petit_white_bg_red.set_background_color(colors.GREEN, copy=True)).render(),
                                 Texte("1)", (100, y_anchor_position+100),
                                       texte_petit_white_bg_red.set_background_color(None, copy=True)).render(),
                                 Texte("2)", (100, y_anchor_position+200),
                                       texte_petit_white_bg_red.set_background_color(None, copy=True)).render(),
                                 Texte("MOYEN", (100, y_anchor_position+300), texte_petit_white_bg_red.set_background_color(
                                     colors.ORANGE, copy=True)).render(),
                                 Texte("3)", (100, y_anchor_position+400),
                                       texte_petit_white_bg_red.set_background_color(None, copy=True)).render(),
                                 Texte("4)", (100, y_anchor_position+500),
                                       texte_petit_white_bg_red.set_background_color(None, copy=True)).render(),
                                 Texte("DIFFICILE", (100, y_anchor_position+600),
                                       texte_petit_white_bg_red.set_background_color(colors.RED, copy=True)).render(),
                                 Texte("5)", (100, y_anchor_position+700),
                                       texte_petit_white_bg_red.set_background_color(None, copy=True)).render()]

        anchor_infos.start_at(t)

        pourcent = random.randint(5,15)
            
        an3 = Annonce(f"Seul {pourcent}% de la population peut avoir 5 sur 5 à ce quiz !", "explosion", self.ia_tts).start_at(t)
        t += an3.duration
        an3.stop_at(t)

        an1 = Annonce("C'est parti !", "sun_glasses", self.ia_tts).start_at(t)
        t += an1.duration
        an1.stop_at(t)
        an2 = Annonce("Niveau facile !", "clin_doeil",self.ia_tts).start_at(t)
        t += an2.duration
        an2.stop_at(t)

        sequence_questions.objects += [anchor_infos, an3 , an1, an2]

        ref_position_reponse = (170, 950)

        for index, item in enumerate(self.json_quizz["questions"]):
            if index == 2:
                an1 = Annonce("Like si c'est trop facile !", "langue", self.ia_tts).start_at(t)
                t+= an1.duration
                an1.stop_at(t)
                an2 = Annonce("On passe au niveau moyen !",
                                  "sourire", self.ia_tts).start_at(t)
                t += an2.duration
                an2.stop_at(t)
                self.sequence.objects += [an1, an2]
                ref_position_reponse = (
                    ref_position_reponse[0], ref_position_reponse[1]+100)
                
            if index == 3:
                an1 = Annonce("N'oublie pas de donner ton score sur 5 en commentaire à la fin !","sun_glasses", self.ia_tts).start_at(t)
                t+=an1.duration
                an1.stop_at(t)
                self.sequence.objects += [an1]

            if index == 4:
                an1 = Annonce("Partage a un ami qui peut avoir 5 sur 5 !", "sourire", self.ia_tts).start_at(t)
                t+=an1.duration
                an1.stop_at(t)
                food = get_random_food()
                an2 = Annonce(f"Si il n'a pas 5 sur 5 il te doit {food} !", "langue", self.ia_tts).start_at(t)
                t+=an2.duration
                an2.stop_at(t)
                an3 = Annonce(
                    "On passe au niveau difficile !", "explosion",self.ia_tts).start_at(t)
                t += an3.duration
                an3.stop_at(t)
                self.sequence.objects += [an1,an2, an3]
                ref_position_reponse = (
                    ref_position_reponse[0], ref_position_reponse[1]+100)

            if "réponse" in item:
                question = Question(item["question"], self.ia_tts).start_at(t)
                t += question.duration
                reponse = Reponse(
                    item["réponse"], ref_position_reponse, self.ia_tts).start_at(t)
                t += reponse.duration
                sequence_questions.objects += [question, reponse]

                ref_position_reponse = (
                    ref_position_reponse[0], ref_position_reponse[1]+100)

        sequence_questions.stop_at(t)

        masque = Basique(mask_color=(87,181,15))
        abonne_toi = Video(root_assets / "video" /"follow.mp4",("center",750), basique=masque, speed=1.8).render().start_at(t-0.5)
        an1 = Annonce("Je sors 2 quiz par jour !", "explosion",self.ia_tts).start_at(t)
        t += an1.duration
        an1.stop_at(t)
        an2 = Annonce("Pense à t'abonner !", "sourire",self.ia_tts).start_at(t)
        t += an2.duration
        an2.stop_at(t)

        self.sequence.objects += [an1, an2]

        logo = Image(root_assets / "image" / "logo.png",("center",550)).render().start_at(t)
       

        self.sequence.objects += [logo, abonne_toi]

        t += 4

        self.sequence.objects = [Background(
            0, t, self.video_background_path)] + self.sequence.objects

        self.sequence.stop_at(t)
