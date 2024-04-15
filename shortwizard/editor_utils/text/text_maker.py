import random

from moviepy.editor import TextClip, ImageClip, vfx
from moviepy.video.fx.resize import resize

from shortwizard.config import root_assets

from shortwizard.editor_utils.Sequence import Sequence
from shortwizard.editor_utils.text import text_utils
from shortwizard.editor_utils.video import video_utils


def create_text_clip_list_dynamic(text, position, t1, t2, font_size, chars_per_line):

    list = text_utils.diviser_texte(text, chars_per_line)

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

        text_clip = TextClip(txt=text1, fontsize=font_size, color=color, stroke_color='black',
                                 stroke_width=5, font='Tiktok-Bold', kerning=-4)

        text_clip = text_clip.set_position(
            (position[0], position[1])).set_duration(delta_per_two_lines/2).set_start(t1+index*delta_per_two_lines)

        text_clip = text_clip.resize(lambda t: video_utils.zoom(t,delta_per_two_lines/4))

        #1
        text_clip_list.append(text_clip)

        text_clip = TextClip(txt=text1, fontsize=font_size, color="white", stroke_color='black',
                                 stroke_width=5, font='Tiktok-Bold', kerning=-4)

        text_clip = text_clip.set_position(
            (position[0], position[1])).set_duration(delta_per_two_lines/2).set_start(t1+index*delta_per_two_lines+delta_per_two_lines/2)

        #2
        text_clip_list.append(text_clip)

        text_clip = TextClip(txt=text2, fontsize=font_size, color="white", stroke_color='black',
                                 stroke_width=5, font='Tiktok-Bold', kerning=-4)

        text_clip = text_clip.set_position(
            (position[0], position[1]+font_size*1.5)).set_duration(delta_per_two_lines/2).set_start(t1+index*delta_per_two_lines)

        #3
        text_clip_list.append(text_clip)

        text_clip = TextClip(txt=text2, fontsize=font_size, color=color, stroke_color='black',
                                 stroke_width=5, font='Tiktok-Bold', kerning=-4)

        text_clip = text_clip.set_position(
            (position[0], position[1]+font_size*1.5)).set_duration(delta_per_two_lines/2).set_start(t1+index*delta_per_two_lines+delta_per_two_lines/2)

        text_clip = text_clip.resize(lambda t: video_utils.zoom(t, delta_per_two_lines/4))
        #4
        text_clip_list.append(text_clip)

    if last_text:
        color = colors[random.randint(0, len(colors)-1)]

        text_clip = TextClip(txt=last_text, fontsize=font_size, color=color, stroke_color='black',
                                 stroke_width=5, font='Tiktok-Bold', kerning=-4)

        text_clip = text_clip.set_position(
            (position[0], position[1])).set_duration(delta_per_two_lines).set_start(t1+delta_per_two_lines*len(list_tuple))
        
        text_clip = text_clip.resize(lambda t: video_utils.zoom(t, delta_per_two_lines/4))

        text_clip_list.append(text_clip)

    return text_clip_list



def create_text(start_time, text, position, color, font_size, chars_per_line):
        list = text_utils.diviser_texte(text, chars_per_line)

        sequence = Sequence(start_time)

        for index, t in enumerate(list):

                text_clip = TextClip(txt=t.upper(), fontsize=font_size, color=color, stroke_color='black',
                                        stroke_width=2, font='Tiktok', kerning=-4)

                text_clip = text_clip.set_position(
                    (position[0], position[1])).set_start(start_time)

                sequence.objects.append(text_clip)
    
        return sequence


def create_text2(start_time, text_content, font_size, chars_per_line, position, font="Tiktok", color="white", background_color=None):

    list = text_utils.diviser_texte(text_content, chars_per_line)

    sequence = Sequence(start_time)

    for index, t in enumerate(list):
            
            text_clip = TextClip(txt=t.upper(), fontsize=font_size, color=color, stroke_color='black',
                                    stroke_width=2, font=font)

            text_clip = text_clip.set_position(
                (position[0], position[1]+index*font_size-7)).set_start(start_time)
            
            if background_color:
                text_frame = text_clip.get_frame(0)
                height, width = text_frame.shape[:2]

                backgroud = text_utils.create_text_background((width+15,font_size+10), 12, background_color)

                backgroud = backgroud.set_position((position[0], position[1]+index*font_size)).set_start(start_time)

                sequence.objects.append(backgroud)

            sequence.objects.append(text_clip)

    return sequence

    

    