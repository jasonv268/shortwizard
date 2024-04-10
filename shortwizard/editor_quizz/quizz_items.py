import random
from pathlib import Path

from shortwizard.config import root
from shortwizard.editor_utils.Item import Item
from shortwizard.editor_utils import Effect

class Question(Item):

    def __init__(self, text_content):
        super().__init__(text_content)

        self.pause_duration = 2.8

        self.font_size = 70

        self.chars_per_line = 22

        self.position = ("center", 700)

        emotes = ["ne_sait_pas_homme", "ne_sait_pas_femme", "bizzare"]

        random_emote = emotes[random.randint(0, len(emotes)-1)]

        self.effects = []

        self.effects = [Effect.AudioEffect(root / Path("shortwizard/assets/audio_effects/swoosh.mp3"), 2, -0.2, 1),
                        Effect.VideoEffect(root / Path("shortwizard/assets/video/chrono.mp4"),
                                           self.pause_duration-0.2, "TTSEND", (200, 700), (138, 255, 2), 0.05),
                        Effect.VideoEffect(root / Path(f"shortwizard/assets/video/{random_emote}.mp4"), self.pause_duration, 2, ("center", 1500), (4, 253, 45), 0)]


class Reponse(Item):
    def __init__(self, text_content):
        super().__init__(text_content)

        self.pause_duration = 1

        self.font_size = 70

        self.chars_per_line = 22

        self.position = ("center", 700)


class Titre(Item):
    def __init__(self, text_content):
        super().__init__(text_content)

        self.pause_duration = 0

        self.font_size = 90

        self.chars_per_line = 15

        self.position = ("center", 200)

        self.effects = []

        self.effects = [Effect.VideoEffect(root / Path("shortwizard/assets/video/follow.mp4"), 11, -0.5, ("center", 1000), (138, 255, 2), 1.0),
                        Effect.VideoEffect(root / Path("shortwizard/assets/video/explosion.mp4"), 1.4, -0.20, ("center", 1500), (4, 253, 45), 0)]


class Annonce(Item):
    def __init__(self, text_content, emotes):
        super().__init__(text_content)

        self.pause_duration = 0

        self.font_size = 90

        self.chars_per_line = 15

        self.position = ("center", 300)

        self.effects = [Effect.VideoEffect(
            root / Path(f"shortwizard/assets/video/{emotes}.mp4"), 1.1, 0, ("center", 50), (4, 253, 45), 0)]