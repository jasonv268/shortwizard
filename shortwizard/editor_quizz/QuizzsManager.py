import json
import random
from shortwizard.utils.Item import Item
from shortwizard.utils import Effect

from shortwizard.config import root
from pathlib import Path


class Question(Item):

    def __init__(self, text_content):
        super().__init__(text_content)

        self.pause_duration = 2.8

        self.font_size = 70

        self.chars_per_line = 22

        self.position = ("center", 700)

        emotes = ["ne_sait_pas_homme", "ne_sait_pas_femme", "bizzare"]

        random_emote = emotes[random.randint(0, len(emotes)-1)]

        self.effects = []

        self.effects = [Effect.AudioEffect(root / Path("shortwizard/assets/audio_effects/swoosh.mp3"), 2, -0.2, 1),
                        Effect.VideoEffect(root / Path("shortwizard/assets/video/chrono.mp4"),
                                           self.pause_duration-0.2, "TTSEND", (200, 700), (138, 255, 2), 0.05),
                        Effect.VideoEffect(root / Path(f"shortwizard/assets/video/{random_emote}.mp4"), self.pause_duration, 2, ("center", 1500), (4, 253, 45), 0)]


class Reponse(Item):
    def __init__(self, text_content):
        super().__init__(text_content)

        self.pause_duration = 1

        self.font_size = 70

        self.chars_per_line = 22

        self.position = ("center", 700)


class Titre(Item):
    def __init__(self, text_content):
        super().__init__(text_content)

        self.pause_duration = 0.2

        self.font_size = 90

        self.chars_per_line = 15

        self.position = ("center", 200)

        self.effects = []

        self.effects = [Effect.VideoEffect(root / Path("shortwizard/assets/video/follow.mp4"), 11, -0.5, ("center", 1000), (138, 255, 2), 1.0),
                        Effect.VideoEffect(root / Path("shortwizard/assets/video/explosion.mp4"), 1.4, -0.20, ("center", 1500), (4, 253, 45), 0)]


class Annonce(Item):
    def __init__(self, text_content, emotes):
        super().__init__(text_content)

        self.pause_duration = 0.1

        self.font_size = 90

        self.chars_per_line = 15

        self.position = ("center", 200)

        self.effects = [Effect.VideoEffect(
            root / Path(f"shortwizard/assets/video/{emotes}.mp4"), 1.1, 0, ("center", -50), (4, 253, 45), 0)]


class Quizz:
    def __init__(self, json_quizz, number):
        if "titre" not in json_quizz:
            raise ValueError("JSON object does not have 'Titre' attribute")
        if "questions" not in json_quizz:
            raise ValueError("JSON object does not have 'questions' attribute")

        self.quizz_name = json_quizz["titre"]

        self.quizz_items: list[Item] = [
            Titre(json_quizz["titre"]), Annonce("C'est parti !", "sun_glasses"), Annonce("On commence facile !", "clin_doeil")]

        self.number = number

        for index, item in enumerate(json_quizz["questions"]):
            if index == 2:
                self.quizz_items.append(
                    Annonce("Like si c'est trop facile !", "langue"))
                self.quizz_items.append(
                    Annonce("On passe au niveau moyen !", "sourire"))

            if index == 4:
                self.quizz_items.append(
                    Annonce("Partage a tes amis !", "sourire"))
                self.quizz_items.append(
                    Annonce("Celui qui a la moins bonne note te paye un kebab !", "langue"))
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


class QuizzsManager:

    def __init__(self, quizzs_path):

        self.group_name = str(quizzs_path).split("/")[-1].replace(".json", "")

        with open(quizzs_path, encoding="utf-8") as text_bank:
            json_quizzs_list = json.load(text_bank)

            self.quizzs = [Quizz(quizz, index)
                           for index, quizz in enumerate(json_quizzs_list)]

    def get_group_name(self):
        return self.group_name

    def get_next_quizz(self) -> Quizz:
        quizz = self.quizzs.pop(0)
        self.current_quizzs = quizz
        return quizz

    def has_next_quizz(self):
        return len(self.quizzs) > 0
