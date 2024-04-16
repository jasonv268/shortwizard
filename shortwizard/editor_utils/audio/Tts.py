from enum import Enum
from pathlib import Path

from moviepy.editor import AudioFileClip

from shortwizard.tts import tts, googletts, watsontts
from shortwizard.file_manager import file_manager

class Mode(Enum):
    GOOGLE_LOW = 0
    GOOGLE_HIGH = 1
    WATSON =3

class Tts:
    def __init__(self, language, mode) -> None:
        self.language = language
        self.mode = mode

    def create_tts(self, text_content):
        tts_func = None

        match self.mode:
            case Mode.GOOGLE_LOW:
                tts_func = tts.generate_voice
            case Mode.GOOGLE_HIGH:
                tts_func = tts.generate_voice
            case Mode.WATSON:
                tts_func = tts.generate_voice
            case _:
                raise ValueError("mode error")
            
        temp_path = file_manager.create_temp_folder() / Path("temp.mp3")

        tts_func(text_content, temp_path)

        audio_file_clip = AudioFileClip(temp_path)

        file_manager.delete_folder(temp_path.parent)

        return audio_file_clip