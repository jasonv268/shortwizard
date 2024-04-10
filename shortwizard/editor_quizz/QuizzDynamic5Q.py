from shortwizard.editor_quizz.Quizz import Quizz
from shortwizard.editor_quizz.quizz_items import Titre, Annonce, Question, Reponse
from shortwizard.text_generator.text_generator import get_random_food

class Quizz5Q(Quizz):
    def __init__(self, json_quizz, number):
        super().__init__(json_quizz, number)

        self.quizz_items += [Annonce("C'est parti !", "sun_glasses"),
                             Annonce("On commence facile !", "clin_doeil")]

        for index, item in enumerate(json_quizz["questions"]):
            if index == 2:
                self.quizz_items.append(
                    Annonce("Like si c'est trop facile !", "langue"))
                self.quizz_items.append(
                    Annonce("On passe au niveau moyen !", "sourire"))

            if index == 4:
                self.quizz_items.append(
                    Annonce("Partage a tes amis !", "sourire"))

                food = get_random_food()
                self.quizz_items.append(
                    Annonce(f"Celui qui a la moins bonne note te paye {food} !", "langue"))

                self.quizz_items.append(
                    Annonce("On passe au niveau difficile !", "explosion"))

            if "réponse" in item:
                self.quizz_items.append(Question(item["question"]))
                self.quizz_items.append(Reponse(item["réponse"]))
            else:
                self.quizz_items.append(Question(item["question"]))

        self.quizz_items.append(
            Annonce("Donne moi ton score sur 5 en commentaire !", "sun_glasses"))
        self.quizz_items.append(Annonce("Pense à t'abonner !", "sourire"))