from shortwizard.editor_utils.audio import Tts
from shortwizard.editor_utils.text import Basique
from shortwizard.editor_utils.Sequence import Sequence
from shortwizard.editor_utils.text import text_maker


class Texte:
    def __init__(self, text_content, position=("center", "center"), basique: Basique.Basique = Basique.default, tts: Tts.Tts | None = None, animation=None) -> None:

        self.text_content = text_content
        self.position = position
        self.basique = basique
        self.tts = tts
        self.animation = animation

    def render(self)->Sequence:            

        if self.tts:
            sequence = Sequence(0)
            audio = self.tts.create_tts(self.text_content)

            if self.animation:
                texte = text_maker.create_text_clip_list_dynamic(self, audio.duration)
            else:
                texte = text_maker.create_text(self)

            sequence.objects += [texte, audio]

            sequence.duration = audio.duration

            return sequence

        else:
            return text_maker.create_text(self)