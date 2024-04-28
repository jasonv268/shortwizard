from shortwizard.editor_utils.Sequence import Sequence
from shortwizard.editor_utils.audio import basique

from shortwizard.editor_utils.audio import audio_maker

class Audio(Sequence):
    def __init__(self, file_path , basique: basique.Basique = basique.default, speed = 1) -> None:
        self.file_path = file_path
        self.basique = basique
        self.speed = speed

        sequence = audio_maker.create_audio(self)

        super().__init__(sequence.start)

        self.duration = sequence.duration
        self.objects = sequence.objects

