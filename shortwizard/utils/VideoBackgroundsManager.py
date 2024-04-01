import os

class VideoBackgoundsManager:
    def __init__(self, video_backgrounds_dir_path):
        self.videos = [video_backgrounds_dir_path / file for file in os.listdir(video_backgrounds_dir_path)]

    def get_video_background_string_path(self):
        path = self.videos.pop(0)
        self.videos.append(path)
        return str(path)