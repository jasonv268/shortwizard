from shortwizard.editor_utils.Sequence import Sequence
from shortwizard.editor_utils.img import Basique, animation

from shortwizard.editor_utils.img import image_maker


class Image(Sequence):
    def __init__(self, file_path, position, basique: Basique.Basique = Basique.default, animation: animation.Animation | None = None) -> None:
        self.file_path = file_path
        self.position = position
        self.basique = basique
        self.animation = animation

        sequence = image_maker.create_image(self)

        super().__init__(sequence.start)

        self.duration = sequence.duration
        self.objects = sequence.objects
