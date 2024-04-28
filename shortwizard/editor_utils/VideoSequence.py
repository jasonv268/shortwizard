from shortwizard.editor_utils.Sequence import Sequence
from moviepy.editor import VideoClip
from moviepy.editor import VideoClip
from shortwizard.editor_utils.img.animation import Animation


class VideoSequence(Sequence):
    def __init__(self, start) -> None:
        super().__init__(start)
        self.position = (540, 960)

    def set_position(self, position):
        self.position = position
        for index, obj in enumerate(self.objects):
            if isinstance(obj, VideoClip):
                self.objects[index] = obj.set_position(position)

            elif isinstance(obj, VideoSequence):
                obj.set_position(position)
        return self
    

    def set_animation(self, animation: Animation):
        animation.set_animation(self)
        self.animation = animation
        return self
