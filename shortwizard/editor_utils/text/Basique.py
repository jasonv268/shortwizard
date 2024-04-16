
class Basique():
    def __init__(self, font, font_size, filling_color, stroke_color, stroke_width, background_color, kerning) -> None:
        self.font = font
        self.font_size = font_size
        self.filling_color = filling_color
        self.stroke_color = stroke_color
        self.stroke_width = stroke_width
        self.background_color = background_color
        self.kerning = kerning

    def set_background_color(self, new_background_color, copy=False):
        if copy:
            new_copy = Basique(self.font, self.font_size, self.filling_color,
                               self.stroke_color, self.stroke_width, new_background_color, self.kerning)
            return new_copy
        else:
            self.background_color = new_background_color
            return self


default = Basique("Tiktok", 70, "white", "black", 3, None, kerning=-3)

texte_petit_white_bg_red = Basique(font="Tiktok",
                                   font_size=70,
                                   filling_color="white",
                                   stroke_color="black",
                                   stroke_width=3,
                                   background_color="red",
                                   kerning=-4)

texte_petit_black_bg_white = Basique(font="Tiktok",
                                     font_size=70,
                                     filling_color="black",
                                     stroke_color="black",
                                     stroke_width=3,
                                     background_color="white",
                                     kerning=-4)

texte_grand_no_bg = Basique(font="Tiktok-Bold",
                            font_size=70,
                            filling_color="white",
                            stroke_color="black",
                            stroke_width=4,
                            background_color=None,
                            kerning=-4)
