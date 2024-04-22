
from shortwizard.editor_utils.img import Basique
from shortwizard.editor_utils.Sequence import Sequence
from shortwizard.editor_utils.video import video_maker
from moviepy.editor import VideoClip
from shortwizard.editor_utils.img.animation import Animation

import copy


class Video(Sequence):

    def __init__(self, file_path, position=(540, 960), basique: Basique.Basique = Basique.default, speed=1.0) -> None:
        self.file_path = file_path
        self.basique = copy.deepcopy(basique)
        self.position = position
        self.speed = speed
        sequence = video_maker.create_video(self)
        super().__init__(sequence.start, sequence.duration, sequence.objects)
        self.set_position(position)
        self.animation = None
        self.basique.set_opacity(self)
        self.basique.set_zoom(self)
        

    def resize(self, size):
        self.basique.set_zoom(self, size)

        return self

    def set_position(self, position):
        self.position = position
        for index, obj in enumerate(self.objects):
            if isinstance(obj, VideoClip):
                self.objects[index] = obj.set_position(position)

            elif isinstance(obj, Video):
                obj.set_position(position)
        return self

    def set_animation(self, animation: Animation):
        animation.set_animation(self)
        self.animation = animation
        return self

    def set_speed(self, speed):
        self.speed = speed
        return self
