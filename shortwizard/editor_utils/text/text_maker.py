import random

from moviepy.editor import TextClip, vfx

from shortwizard.editor_utils.Sequence import Sequence
from shortwizard.editor_utils.text import text_utils, texte
from shortwizard.editor_utils.video import video_utils

from shortwizard.editor_utils import colors as colors_manager

from skimage.filters import gaussian



def create_text_clip_list_dynamic(texte: 'texte.Texte', tts_duration) -> Sequence:

    sequence = Sequence(0)

    chars_per_line = text_utils.get_chars_per_line(texte)

    list = text_utils.diviser_texte(texte.text_content, chars_per_line)

    start_position = texte.position

    text_clip_list = []

    colors = colors_manager.get_all()

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

    chars_per_line = text_utils.get_chars_per_line(texte)

    list = text_utils.diviser_texte(texte.text_content, chars_per_line)

    start_position = texte.position

    text_clip_list = []

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

        text_clip_list.append(text_clip)

    for text_clip in text_clip_list:
        sequence.objects.append(text_clip)

    return sequence
