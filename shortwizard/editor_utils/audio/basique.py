class Basique:
    def __init__(self, volume=1.0, fade_in=0, fade_out=0) -> None:
        self.volume = volume
        self.fade_in = fade_in
        self.fade_out = fade_out


default = Basique()