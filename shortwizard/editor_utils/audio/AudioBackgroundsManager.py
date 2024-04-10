import os

class AudioBackgroundsManager:
    def __init__(self, audio_backgrounds_dir_path):
        self.videos = [audio_backgrounds_dir_path / file for file in os.listdir(audio_backgrounds_dir_path)]

    def get_audio_background_path(self):
        path = self.videos.pop(0)
        self.videos.append(path)
        return str(path)