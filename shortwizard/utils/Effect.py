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

    def __init__(self,path,  duration, start_time, position):
        super().__init__(path, duration, start_time)

        self.position = position

    def get_position(self):
        return self.position


class ImageEffect(Effect):

    def __init__(self,path, duration, start_time, position):
        super().__init__(path, duration, start_time)

        self.position = position

    def get_position(self):
        return self.position


class AudioEffect(Effect):

    def __init__(self, path, duration, start_time):
        super().__init__(path, duration, start_time)

