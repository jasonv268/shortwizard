
from shortwizard.editor_utils.img import Basique
from shortwizard.editor_utils.Sequence import Sequence
from shortwizard.editor_utils.video import video_maker


class Video:

    def __init__(self, file_path, position, basique: Basique.Basique = Basique.default, animation=None, speed=1.0) -> None:
        self.file_path = file_path
        self.position = position
        self.basique = basique
        self.animation = animation
        self.speed = speed


    def render(self)->Sequence:
        
        return video_maker.create_video(self)

    
