from shortwizard.editor_utils.text import Basique, Tts
from shortwizard.editor_utils.Sequence import Sequence

class Texte(Sequence):
    def __init__(self, text_content, basique: Basique.Basique, tts: Tts.Tts) -> None:
        
        self.text_content = text_content
        self.basique = basique
        self.tts = tts