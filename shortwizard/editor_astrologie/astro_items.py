import random
from pathlib import Path

from shortwizard.config import root
from shortwizard.editor_utils.Item import Item
from shortwizard.editor_utils import Effect

class Titre(Item):
    def __init__(self, text_content):
        super().__init__(text_content)

        self.pause_duration = 0

        self.font_size = 90

        self.chars_per_line = 15

        self.position = ("center", 200)

        self.effects = []

        self.effects = [Effect.VideoEffect(root / Path("shortwizard/assets/video/follow.mp4"), 11, -0.5, ("center", 1000), (138, 255, 2), 1.0)]


class Annonce(Item):
    def __init__(self, text_content, emotes):
        super().__init__(text_content)

        self.pause_duration = 0.1

        self.font_size = 90

        self.chars_per_line = 15

        self.position = ("center", 300)

        self.effects = [Effect.VideoEffect(
            root / Path(f"shortwizard/assets/video/{emotes}.mp4"), 1.1, 0, ("center", 50), (4, 253, 45), 0)]