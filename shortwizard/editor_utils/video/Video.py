
from moviepy.editor import VideoFileClip
from shortwizard.editor_utils.VideoSequence import VideoSequence

from shortwizard.editor_utils.img import Basique

import copy

class Video(VideoSequence):

    def __init__(self, file_path) -> None:
        self.file_path = file_path

        super().__init__(0)

        self.objects = [VideoFileClip(file_path)]

        self.basique = Basique.Basique()
        self.basique.link_sequence(self)

        self.speed = 1.0

    def set_basique(self, basique: Basique.Basique):
        print("set basique")
        print(self.objects)

        self.basique = copy.deepcopy(basique)
        self.basique.link_sequence(self)
        self.basique.set_all()
        return self

    def set_speed(self, speed):
        self.speed = speed

        def set_mask_speed_rec(sequence):
            for index, obj in enumerate(sequence.objects):
                if isinstance(obj, VideoFileClip):
                    sequence.objects[index] = obj.speedx(self.speed)
                elif isinstance(obj, VideoSequence):
                    set_mask_speed_rec(obj)

        set_mask_speed_rec(self)

        return self
