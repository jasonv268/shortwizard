from abc import ABC, abstractmethod
from typing import Union
from enum import Enum
        

class Effect(ABC):

    def __init__(self,effect_path, duration, start_time):
        self.effect_path = effect_path
        self.duration = duration
        self.start_time = start_time

    def has_duration(self):
        return self.duration is not None

    def get_duration(self):
        return self.duration

    def get_effect_path(self):
        return str(self.effect_path)
    
    def get_start_time(self):
        return self.start_time


class VideoEffect(Effect):

    def __init__(self,path,  duration, start_time, position, mask_color:tuple[int,int,int], volume:float):
        super().__init__(path, duration, start_time)

        self.position = position

        self.mask_color = mask_color

        self.volume = volume

    def get_position(self):
        return self.position
    
    def get_mask_color(self):
        return self.mask_color
    
    def get_volume(self):
        return self.volume


class ImageEffect(Effect):

    def __init__(self,path, duration, start_time, position, mask_color:tuple[int,int,int]):
        super().__init__(path, duration, start_time)

        self.position = position

        self.mask_color = mask_color

    def get_position(self):
        return self.position
    
    def get_mask_color(self):
        return self.mask_color


class AudioEffect(Effect):

    def __init__(self, path, duration, start_time, volume:float):
        super().__init__(path, duration, start_time)

        self.volume = volume

    def get_volume(self):
        return self.volume

