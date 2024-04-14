# from shortwizard.editor_quizz.Quizz import Quizz
# from shortwizard.editor_quizz.quizz_items import Titre, Annonce, Question, Reponse
# from shortwizard.text_generator.text_generator import get_random_food

# class QuizzCouple(Quizz):
#     def __init__(self, json_quizz, number):
#         super().__init__(json_quizz, number)

#         for index, item in enumerate(json_quizz["questions"]):

#             if "réponse" in item:
#                 self.quizz_items.append(Question(item["question"]))
#                 self.quizz_items.append(Reponse(item["réponse"]))
#             else:
#                 self.quizz_items.append(Question(item["question"]))

#         self.quizz_items.append(
#             Annonce("Partage à ton ou ta partenaire !", "sun_glasses"))