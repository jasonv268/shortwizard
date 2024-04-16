from shortwizard.editor_utils.Sequence import Sequence
from shortwizard.editor_utils.audio import basique

class Audio:
    def __init__(self, file_path , basique: basique.Basique = basique.default, speed = 1) -> None:
        self.file_path = file_path
        self.basique = basique
        self.speed = speed


    def render(self) -> Sequence:

        return Sequence(0)
