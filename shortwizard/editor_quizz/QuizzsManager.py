from enum import Enum
import json
from shortwizard.editor_quizz.Quizz import Quizz
from shortwizard.editor_quizz.QuizzDynamic5Q import Quizz5Q
from shortwizard.editor_quizz.QuizzCouple import QuizzCouple

class QuizzType(Enum):
    DYNAMIC5Q = 0
    COUPLE = 1
    
class QuizzsManager:

    def __init__(self, quizzs_path, quizz_type):

        match quizz_type:
            case QuizzType.DYNAMIC5Q:
                QuizzClass = Quizz5Q
            case QuizzType.COUPLE:
                QuizzClass = QuizzCouple
            case _:
                raise ValueError("quizz_type error")
        

        self.group_name = str(quizzs_path).split("/")[-1].replace(".json", "")

        with open(quizzs_path, encoding="utf-8") as text_bank:
            json_quizzs_list = json.load(text_bank)

            if isinstance(json_quizzs_list, list):
                self.quizzs = [QuizzClass(quizz, index)
                               for index, quizz in enumerate(json_quizzs_list)]
            else:
                self.quizzs = [QuizzClass(json_quizzs_list, 0)]

    def get_group_name(self):
        return self.group_name

    def get_next_quizz(self) -> Quizz:
        quizz = self.quizzs.pop(0)
        self.current_quizzs = quizz
        return quizz

    def has_next_quizz(self):
        return len(self.quizzs) > 0
