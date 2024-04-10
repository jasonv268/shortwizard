from shortwizard.editor_astrologie.astro_items import Titre, Annonce
from shortwizard.editor_utils.Item import Item


class Astrologie:

    def __init__(self, json_astro, number):
        if "titre" not in json_astro:
            raise ValueError("JSON object does not have 'Titre' attribute")
        if "textes" not in json_astro:
            raise ValueError("JSON object does not have 'questions' attribute")

        self.quizz_name = json_astro["titre"]

        self.quizz_items: list[Item] = [Titre(json_astro["titre"])]

        self.number = number

        for index, item in enumerate(json_astro["textes"]):
                self.quizz_items.append(Annonce(item["texte"],"explosion"))


        self.quizz_items.append(
            Annonce("Partage à ton ou ta partenaire !", "sun_glasses"))

    def get_title(self):
        return self.quizz_name

    def get_number(self):
        return self.number

    def get_next_item(self):
        return self.quizz_items.pop(0)

    def has_next_item(self):
        return len(self.quizz_items) > 0

    def get_all_items(self):
        return self.quizz_items