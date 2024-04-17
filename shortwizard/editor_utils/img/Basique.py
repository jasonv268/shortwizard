class Basique:
    def __init__(self, mask_color=None, opacity=1.0, zoom=1.0) -> None:
        self.mask_color = mask_color
        self.opacity = opacity
        self.zoom = zoom


default = Basique()
