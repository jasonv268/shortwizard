#from shortwizard.editor_utils.MyTextClip import MyTextClip, TtsTextClip
from shortwizard.editor_utils.Sequence import Sequence


class Quizz:

    def __init__(self, json_quizz, number):
        if "titre" not in json_quizz:
            raise ValueError("JSON object does not have 'Titre' attribute")
        if "questions" not in json_quizz:
            raise ValueError("JSON object does not have 'questions' attribute")

        self.quizz_name = json_quizz["titre"]

        self.json_quizz = json_quizz

        self.sequence = Sequence(0)

        self.number = number

    def get_title(self):
        return self.quizz_name

    def get_number(self):
        return self.number
    

    def get_sequence(self):
        return self.sequence

    
   