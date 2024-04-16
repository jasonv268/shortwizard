import random

from moviepy.editor import TextClip

from shortwizard.config import root_assets

from shortwizard.editor_utils.Sequence import Sequence
from shortwizard.editor_utils.text import text_utils, texte
from shortwizard.editor_utils.video import video_utils


def create_text_clip_list_dynamic(texte: 'texte.Texte', tts_duration) -> Sequence:

    sequence = Sequence(0)

    if texte.basique.font_size <= 70:
        chars_per_line = 20
    else:
        chars_per_line = 15

    list = text_utils.diviser_texte(texte.text_content, chars_per_line)

    start_position = texte.position

    text_clip_list = []

    # Vert Bleu Jaune Orange Rouge

    colors = ["rgba(55,226,101,255)", "rgba(68,143,234,255)",
              "rgba(251,221,22,255)", "rgba(244,171,40,255)", "rgba(255,22,0,255)"]

    line_number = len(list)

    last_text = None

    delta_per_two_lines = 0

    if line_number % 2 == 1:
        last_text = list.pop()
        delta_per_two_lines = (tts_duration)/(line_number//2+1)

    else:
        delta_per_two_lines = (tts_duration)/(line_number//2)

    list_tuple = [(list[i], list[i+1]) for i in range(0, len(list), 2)]

    for index, (text1, text2) in enumerate(list_tuple):

        color = colors[random.randint(0, len(colors)-1)]

        text_clip = TextClip(text1, fontsize=texte.basique.font_size, color=color, stroke_color=texte.basique.stroke_color,
                             stroke_width=texte.basique.stroke_width, font=texte.basique.font, kerning=texte.basique.kerning)

        text_clip = text_clip.set_position(
            (start_position[0], start_position[1])).set_duration(delta_per_two_lines/2).set_start(index*delta_per_two_lines)

        text_clip = text_clip.resize(
            lambda t: video_utils.zoom(t, delta_per_two_lines/4))

        # 1
        text_clip_list.append(text_clip)

        text_clip = TextClip(text1, fontsize=texte.basique.font_size, color="white", stroke_color=texte.basique.stroke_color,
                             stroke_width=texte.basique.stroke_width, font=texte.basique.font, kerning=texte.basique.kerning)

        text_clip = text_clip.set_position(
            (start_position[0], start_position[1])).set_duration(delta_per_two_lines/2).set_start(index*delta_per_two_lines+delta_per_two_lines/2)

        # 2
        text_clip_list.append(text_clip)

        text_clip = TextClip(text2, fontsize=texte.basique.font_size, color="white", stroke_color=texte.basique.stroke_color,
                             stroke_width=texte.basique.stroke_width, font=texte.basique.font, kerning=texte.basique.kerning)

        text_clip = text_clip.set_position(
            (start_position[0], start_position[1]+texte.basique.font_size*1.5)).set_duration(delta_per_two_lines/2).set_start(index*delta_per_two_lines)

        # 3
        text_clip_list.append(text_clip)

        text_clip = TextClip(text2, fontsize=texte.basique.font_size, color=color, stroke_color=texte.basique.stroke_color,
                             stroke_width=texte.basique.stroke_width, font=texte.basique.font, kerning=texte.basique.kerning)

        text_clip = text_clip.set_position(
            (start_position[0], start_position[1]+texte.basique.font_size*1.5)).set_duration(delta_per_two_lines/2).set_start(index*delta_per_two_lines+delta_per_two_lines/2)

        text_clip = text_clip.resize(
            lambda t: video_utils.zoom(t, delta_per_two_lines/4))
        # 4
        text_clip_list.append(text_clip)

    if last_text:
        color = colors[random.randint(0, len(colors)-1)]

        text_clip = TextClip(last_text, fontsize=texte.basique.font_size, color=color, stroke_color=texte.basique.stroke_color,
                             stroke_width=texte.basique.stroke_width, font=texte.basique.font, kerning=texte.basique.kerning)

        text_clip = text_clip.set_position(
            (start_position[0], start_position[1])).set_duration(delta_per_two_lines).set_start(delta_per_two_lines*len(list_tuple))

        text_clip = text_clip.resize(
            lambda t: video_utils.zoom(t, delta_per_two_lines/4))

        text_clip_list.append(text_clip)

    sequence.objects = text_clip_list

    return sequence


def create_text(texte: 'texte.Texte') -> Sequence:
    sequence = Sequence(0)

    if texte.basique.font_size <= 70:
        chars_per_line = 25
    else:
        chars_per_line = 20

    list = text_utils.diviser_texte(texte.text_content, chars_per_line)

    start_position = texte.position

    for index, t in enumerate(list):

        text_clip = TextClip(t, fontsize=texte.basique.font_size, color=texte.basique.filling_color, stroke_color=texte.basique.stroke_color,
                             stroke_width=texte.basique.stroke_width, font=texte.basique.font).set_start(0)

        text_clip = text_clip.set_position(
            (start_position[0], start_position[1]+index*texte.basique.font_size-7))

        if texte.basique.background_color:
            text_frame = text_clip.get_frame(0)
            height, width = text_frame.shape[:2]

            backgroud = text_utils.create_text_background(
                (width+15, texte.basique.font_size+10), 12, texte.basique.background_color)

            backgroud = backgroud.set_position(
                (start_position[0], start_position[1]+index*texte.basique.font_size))

            sequence.objects.append(backgroud)

        sequence.objects.append(text_clip)

    return sequence
