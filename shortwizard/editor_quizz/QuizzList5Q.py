from shortwizard.editor_quizz.Quizz import Quizz
from shortwizard.editor_quizz.quizz_items import *
from shortwizard.editor_utils.Sequence import Sequence
from shortwizard.text_generator.text_generator import get_random_food


class QuizzList5Q(Quizz):

    def __init__(self, json_quizz, number):
        super().__init__(json_quizz, number)

    def set_background_path(self, path):
        self.video_background_path = path

    def create_sequence(self):
        t=0

        title = Title(self.json_quizz["titre"], 0)

        anchor_tag = text_maker.create_text2(start_time=t,text_content="@quizz_pour_tous", font_size=70, chars_per_line=25, position=("center", 1700),color="black", background_color="white")

        self.sequence.objects += [title, anchor_tag]

        t+=title.duration

        sequence_questions = Questions(t)
        self.sequence.objects += [sequence_questions]

        anchor_title = text_maker.create_text2(start_time=t,text_content=self.json_quizz["titre"], font_size=70, chars_per_line=25, position=("center", 75), background_color="red")

        sequence_questions.objects += [anchor_title]

        ref_position_reponse = (120, 950)

        for index, item in enumerate(self.json_quizz["questions"]):
            if index ==2:
                annonce = Annonce("On passe au niveau moyen !", t)
                self.sequence.objects += [annonce]
                t+=annonce.duration
                ref_position_reponse = (ref_position_reponse[0], ref_position_reponse[1]+100)

            if index == 4:
                annonce = Annonce("On passe au niveau difficile !", t)
                self.sequence.objects += [annonce]
                t+=annonce.duration
                ref_position_reponse = (ref_position_reponse[0], ref_position_reponse[1]+100)

            if "réponse" in item:
                question = Question(item["question"], t)
                t+=question.duration
                reponse = Reponse(item["réponse"], t,ref_position_reponse)
                t+=reponse.duration
                sequence_questions.objects += [question, reponse]

                ref_position_reponse = (ref_position_reponse[0], ref_position_reponse[1]+100)

        sequence_questions.stop_at(t)

        t += 3

        self.sequence.objects = [Background(0, t, self.video_background_path)] + self.sequence.objects
        self.sequence.stop_at(t)

