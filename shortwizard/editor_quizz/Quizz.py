from shortwizard.editor_utils.MyTextClip import MyTextClip, TtsTextClip
from shortwizard.editor_utils.Sequence import Sequence


class Quizz:

    def __init__(self, json_quizz, number):
        if "titre" not in json_quizz:
            raise ValueError("JSON object does not have 'Titre' attribute")
        if "questions" not in json_quizz:
            raise ValueError("JSON object does not have 'questions' attribute")

        self.quizz_name = json_quizz["titre"]

        self.quizz_items = []

        self.sequence = Sequence()

        self.number = number

    def get_title(self):
        return self.quizz_name

    def get_number(self):
        return self.number

    def get_next_item(self):
        return self.quizz_items.pop(0)

    def has_next_item(self):
        return len(self.quizz_items) > 0
    
    def get_sequence(self)->Sequence:
        return self.sequence

    def get_all_items(self):
        return self.quizz_items
    
    def get_tts_items(self):
        return [item for item in self.quizz_items if isinstance(item, TtsTextClip)]
    