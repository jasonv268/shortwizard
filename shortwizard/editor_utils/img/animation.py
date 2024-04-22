from math import sin
import math

from shortwizard.editor_utils.Sequence import Sequence
from moviepy.editor import VideoClip


class Animation:
    def __init__(self, position_func=None, size_func=None) -> None:
        self.position_func = position_func
        self.size_func = size_func
        self.sequence: Sequence = Sequence(0)


    def set_sequence(self, sequence: Sequence):
        self.sequence = sequence
        return self
    
    def set_animation(self, sequence):
        if (self.position_func):
            self.position_func = self.position_func

        if (self.size_func):
            self.size_func = self.size_func

        def set_animation_rec(self,sequence):
            for index, obj in enumerate(sequence.objects):
                if isinstance(obj, VideoClip):
                    if (self.size_func):
                        sequence.objects[index] = obj.resize(self.size_func)

                    if (self.position_func):

                        

                        position_fun = lambda t: self.position_func(sequence.position[0],sequence.position[1], t)

                        sequence.objects[index] = obj.set_position(position_fun)

                elif isinstance(obj, Sequence):
                    set_animation_rec(self,obj)

        set_animation_rec(self,sequence)
          
        return self

battement = Animation(size_func=lambda t: (1 + sin(10 * t) * 0.2),
                      position_func=lambda x, y, t: (x, y + sin(10 * t) * (-50)))

slide = Animation(position_func=lambda x, y, t: (x-100 + t*50, y)
                  if x - t*50 < x+50 else (x-100 + t*50, y))
