import numpy as np

import moviepy.editor as mpe
from PIL import Image, ImageDraw, ImageColor


def create_text_background(size, radius, color):

    def rounded_rectangle(size, radius, color):
        """Create a rounded rectangle image."""
        color = ImageColor.getrgb(color)
        width, height = size
        img = Image.new("RGBA", size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        draw.rectangle([(radius, 0), (width - radius, height)], fill=color)
        draw.rectangle([(0, radius), (width, height - radius)], fill=color)
        draw.pieslice([(0, 0), (radius * 2, radius * 2)], 180, 270, fill=color)
        draw.pieslice([(width - radius * 2, 0),
                      (width, radius * 2)], 270, 360, fill=color)
        draw.pieslice([(0, height - radius * 2),
                      (radius * 2, height)], 90, 180, fill=color)
        draw.pieslice([(width - radius * 2, height - radius * 2),
                      (width, height)], 0, 90, fill=color)
        return img

    rounded_rect = rounded_rectangle(size, radius, color)

    # Convertir l'image PIL en tableau numpy
    rounded_rect_array = np.array(rounded_rect)

    return mpe.ImageClip(rounded_rect_array, ismask=False)


def diviser_texte(texte, longueur_max):
    mots = texte.split(' ')
    parties = []
    partie_actuelle = ""

    for mot in mots:
        if len(partie_actuelle) + len(mot) + 1 <= longueur_max:  # Ajoute 1 pour l'espace
            if partie_actuelle:  # Ajoute un espace si nécessaire
                partie_actuelle += " "
            partie_actuelle += mot
        else:
            parties.append(partie_actuelle)
            partie_actuelle = mot

    if partie_actuelle:  # Ajoute la dernière partie
        parties.append(partie_actuelle)

    return parties


def get_chars_per_line(font_size):
    if 0 < font_size <= 70:
        return 19
    elif 70 < font_size <= 80:
        return 17
    elif 80 < font_size <= 90:
        return 15
    else:
        return 13