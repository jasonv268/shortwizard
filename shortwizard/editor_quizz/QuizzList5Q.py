from shortwizard.editor_quizz.Quizz import Quizz
from shortwizard.editor_quizz.quizz_items import *
from shortwizard.editor_utils.Sequence import Sequence
from shortwizard.text_generator.text_generator import get_random_food


class QuizzList5Q(Quizz):
    def __init__(self, json_quizz, number):
        super().__init__(json_quizz, number)

        # effet de flou avec zoom entrant
        # annonces
        # mise en place de texte ancré
        # annonces
        # for q in qs:
        # question tts q
        # reponse tts q
        #  reponse ancré q
        #
        # annonces fin

        self.sequence.objects += title(json_quizz["titre"], 0)

        t = 2

        sequence_questions = Questions(t)
        self.sequence.objects += [sequence_questions]

        for index, item in enumerate(json_quizz["questions"]):
            if "réponse" in item:
                sequence_questions.add_question(item["question"], t)
                sequence_questions.add_reponse(item["réponse"], t+2)
                t += 5
            else:
                sequence_questions.add_question(item["question"], t)
                t += 2

        sequence_questions.stop_at(t)

        t += 7

        self.sequence.objects = [Background(0, t)] + self.sequence.objects
        self.sequence.stop_at(t)

