import moviepy.editor as mpe
import random

from shortwizard.editor_utils.video import video_utils


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


def create_text_clip_list_hooked(text, position, t1, font_size, chars_per_line):

    list = diviser_texte(text, chars_per_line)

    text_clip_list = []

    for index, t in enumerate(list):
        text_clip = mpe.TextClip(txt=t, fontsize=font_size, color='red', stroke_color='black',
                                 stroke_width=5, font='Tiktok-Bold', kerning=-4)

        text_clip = text_clip.set_position(
            (position[0], position[1]+index*font_size*2)).set_duration(None).set_start(t1-1)

        text_clip_list.append(text_clip)

    return text_clip_list


def create_text_clip_list(text, position, t1, t2, font_size, chars_per_line):

    list = diviser_texte(text, chars_per_line)

    text_clip_list = []

    for index, t in enumerate(list):
        text_clip = mpe.TextClip(txt=t, fontsize=font_size, color='white', stroke_color='black',
                                 stroke_width=5, font='Tiktok-Bold', kerning=-4)

        text_clip = text_clip.set_position(
            (position[0], position[1]+index*font_size*2)).set_duration((t2-t1)).set_start(t1-1)

        text_fadein = text_clip.crossfadein(0.5)

        # Appliquer un fondu en sortie
        text_fadeout = text_fadein.crossfadeout(0.5)

        text_clip2 = mpe.TextClip(
            txt=t, fontsize=font_size, color='black', font='Tiktok-Bold', kerning=-4)

        text_clip2 = text_clip2.set_position(
            (position[0], 10+position[1]+index*font_size*2)).set_duration((t2-t1)).set_start(t1-1)

        text_fadein2 = text_clip2.crossfadein(0.5)

        # Appliquer un fondu en sortie
        text_fadeout2 = text_fadein2.crossfadeout(0.5)

        text_fadeout2 = text_fadeout2.set_opacity(0.25)

        text_clip_list.append(text_fadeout2)
        text_clip_list.append(text_fadeout)

    return text_clip_list


def create_text_clip_list_dynamic(text, position, t1, t2, font_size, chars_per_line):

    list = diviser_texte(text, chars_per_line)

    text_clip_list = []

    # Vert Bleu Jaune Orange Rouge

    colors = ["rgba(55,226,101,255)", "rgba(68,143,234,255)",
              "rgba(251,221,22,255)", "rgba(244,171,40,255)", "rgba(255,22,0,255)"]

    line_number = len(list)

    last_text = None

    delta_per_two_lines = 0

    if line_number % 2 == 1:
        last_text = list.pop()
        delta_per_two_lines = (t2-t1)/(line_number//2+1)

    else:
        delta_per_two_lines = (t2-t1)/(line_number//2)

    list_tuple = [(list[i], list[i+1]) for i in range(0, len(list), 2)]

    for index, (text1, text2) in enumerate(list_tuple):

        color = colors[random.randint(0, len(colors)-1)]

        text_clip = mpe.TextClip(txt=text1, fontsize=font_size, color=color, stroke_color='black',
                                 stroke_width=5, font='Tiktok-Bold', kerning=-4)

        text_clip = text_clip.set_position(
            (position[0], position[1])).set_duration(delta_per_two_lines/2).set_start(t1+index*delta_per_two_lines)

        text_clip = text_clip.resize(lambda t: video_utils.resize(t,delta_per_two_lines/2))

        #1
        text_clip_list.append(text_clip)

        text_clip = mpe.TextClip(txt=text1, fontsize=font_size, color="white", stroke_color='black',
                                 stroke_width=5, font='Tiktok-Bold', kerning=-4)

        text_clip = text_clip.set_position(
            (position[0], position[1])).set_duration(delta_per_two_lines/2).set_start(t1+index*delta_per_two_lines+delta_per_two_lines/2)

        #2
        text_clip_list.append(text_clip)

        text_clip = mpe.TextClip(txt=text2, fontsize=font_size, color="white", stroke_color='black',
                                 stroke_width=5, font='Tiktok-Bold', kerning=-4)

        text_clip = text_clip.set_position(
            (position[0], position[1]+font_size*2)).set_duration(delta_per_two_lines/2).set_start(t1+index*delta_per_two_lines)

        #3
        text_clip_list.append(text_clip)

        text_clip = mpe.TextClip(txt=text2, fontsize=font_size, color=color, stroke_color='black',
                                 stroke_width=5, font='Tiktok-Bold', kerning=-4)

        text_clip = text_clip.set_position(
            (position[0], position[1]+font_size*2)).set_duration(delta_per_two_lines/2).set_start(t1+index*delta_per_two_lines+delta_per_two_lines/2)

        text_clip = text_clip.resize(lambda t: video_utils.resize(t, delta_per_two_lines/2))
        #4
        text_clip_list.append(text_clip)

    if last_text:
        color = colors[random.randint(0, len(colors)-1)]

        text_clip = mpe.TextClip(txt=last_text, fontsize=font_size, color=color, stroke_color='black',
                                 stroke_width=5, font='Tiktok-Bold', kerning=-4)

        text_clip = text_clip.set_position(
            (position[0], position[1])).set_duration(delta_per_two_lines).set_start(t1+delta_per_two_lines*len(list_tuple))
        
        text_clip = text_clip.resize(lambda t: video_utils.resize(t, delta_per_two_lines/2))

        text_clip_list.append(text_clip)

    return text_clip_list

