from abc import ABC, abstractmethod
from shortwizard.utils import Effect


class Item(ABC):

    def __init__(self, text_content):
        self.text_content = text_content
        self.tts_path = None
        self.effects: list[Effect.Effect ]= []
        self.pause_duration = 0
        self.font_size = 48
        self.chars_per_line = 30
        self.position = ("center",960-self.font_size*2)

    def get_text_content(self):
        return self.text_content

    def has_tts_path(self):
        return self.tts_path is not None

    def get_tts_path(self):
        return self.tts_path

    def set_tts_path(self, tts_path):
        self.tts_path = tts_path

    def get_pause_duration(self):
        return self.pause_duration
    
    def has_effects(self):
        return len(self.effects)>0
    
    def get_effects(self)->list[Effect.Effect]:
        return self.effects

    def get_font_size(self):
        return self.font_size
    
    def get_chars_per_line(self):
        return self.chars_per_line
    
    def get_position(self):
        return self.position