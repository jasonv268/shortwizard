from shortwizard.editor_utils.MyTextClip import MyTextClip, TtsTextClip
import moviepy.editor as mpe
from shortwizard.editor_utils.Sequence import Sequence
from shortwizard.editor_utils.text import text_utils
from shortwizard.editor_utils.video import VideoBackgroundsManager
from shortwizard.editor_utils.video import video_utils

import os
from pathlib import Path
from shortwizard.editor_utils import Effect
from shortwizard.config import root
from shortwizard.editor_utils.audio import AudioBackgroundsManager


def create_effects(effects: list[Effect.Effect], start_time, tts_duration):

    audio_clip_list, video_clip_list = [], []

    for effect in effects:
        if isinstance(effect, Effect.AudioEffect):

            sound_effect = mpe.AudioFileClip(
                effect.get_effect_path())

            if effect.get_start_time() == "TTSEND":
                sound_effect = sound_effect.set_start(
                    start_time+tts_duration)

            else:
                sound_effect = sound_effect.set_start(
                    start_time+effect.get_start_time())

            sound_effect = sound_effect.set_duration(
                min(effect.get_duration(), sound_effect.duration))

            sound_effect = sound_effect.volumex(effect.get_volume())

            audio_clip_list.append(sound_effect)

        elif isinstance(effect, Effect.ImageEffect):

            image_effect = mpe.ImageClip(
                effect.get_effect_path(), effect.get_position())
            image_effect = image_effect.set_position(effect.get_position())

            if effect.get_start_time() == "TTSEND":
                image_effect = image_effect.set_start(
                    tts_duration+start_time)
            else:
                image_effect = image_effect.set_start(
                    effect.get_start_time()+start_time)

            image_effect: mpe.ImageClip = image_effect.set_duration(
                min(effect.get_duration(), sound_effect.duration))

            video_clip_list.append(image_effect)

        elif isinstance(effect, Effect.VideoEffect):

            video_effect = mpe.VideoFileClip(effect.get_effect_path())
            video_effect = video_utils.remove_green_screen(
                video_effect, effect)

            if effect.get_start_time() == "TTSEND":
                video_effect = video_effect.set_start(
                    tts_duration+start_time)
            else:
                video_effect = video_effect.set_start(
                    effect.get_start_time()+start_time)

            video_effect: mpe.VideoFileClip = video_effect.set_duration(
                min(effect.get_duration(), video_effect.duration))

            video_effect = video_effect.volumex(effect.get_volume())

            video_clip_list.append(video_effect)

    return audio_clip_list, video_clip_list


def create_audio_and_text(item_list: list[MyTextClip], text_clip_function):

    time = 0.5

    audio_clip_list = []

    video_clip_list = []

    for item in item_list:

        if isinstance(item, TtsTextClip):

            audio_part = mpe.AudioFileClip(item.get_tts_path())
            audio_part = audio_part.set_start(time)

            sound_effects = []

            if item.has_effects():

                effects = item.get_effects()

                audio_effects_clip, video_effects_clip = create_effects(
                    effects, time, audio_part.duration)

                sound_effects += audio_effects_clip

                video_clip_list += video_effects_clip

            audio_clip_list.append(audio_part)
            audio_clip_list = audio_clip_list + sound_effects

            video_clip_list += text_clip_function(
                item.get_text_content().upper(), item.get_position(), time, time+audio_part.duration, item.get_font_size(), item.get_chars_per_line())

            time = time + audio_part.duration + item.get_pause_duration()

        else:

            text_clip_list = text_utils.create_text_clip_list_hooked(item.get_text_content(
            ).upper(), item.get_position(), time, item.get_font_size(), item.get_chars_per_line())

            video_clip_list += text_clip_list

    audio_clip = mpe.CompositeAudioClip(audio_clip_list)

    return audio_clip, video_clip_list


def create_bg(vbm: VideoBackgroundsManager.VideoBackgoundsManager, short_duration):

    bg_clip = mpe.VideoFileClip(vbm.get_video_background_string_path())

    bg_clip = video_utils.crop_bg(bg_clip)

    bg_clip = video_utils.fade_in_out_bg(bg_clip)

    if bg_clip.duration > short_duration:
        bg_clip = bg_clip.subclip(0, short_duration)
        bg_clip = video_utils.fade_in_out_bg(bg_clip)

    else:
        while bg_clip.duration < short_duration:
            bg_aux = mpe.VideoFileClip(vbm.get_video_background_string_path())
            if bg_aux.duration > short_duration - bg_clip.duration:
                bg_aux_duration = short_duration - bg_clip.duration
                if bg_aux_duration < 2:
                    bg_aux_duration = 2
                bg_aux = bg_aux.subclip(0, bg_aux_duration)
            bg_aux = video_utils.crop_bg(bg_aux)
            bg_aux = video_utils.fade_in_out_bg(bg_aux)
            bg_clip = mpe.concatenate_videoclips([bg_clip, bg_aux])

    return bg_clip


def write_final_render(bg_clip, text_clip_list, audio_clip, output_dir, file_name):

    final_render: mpe.CompositeVideoClip = mpe.CompositeVideoClip(
        [bg_clip]+text_clip_list, bg_color=None)

    final_render = final_render.set_audio(
        mpe.CompositeAudioClip([final_render.audio, audio_clip])).set_duration(bg_clip.duration)

    final_render.write_videofile(
        os.path.normpath(Path(output_dir) / Path(f"{file_name}.mp4")), codec="libx264", threads=4, fps=24)

    audio_clip.close()
    final_render.close()
    for clip in text_clip_list:
        clip.close()

def write_final_render2(objects: list[Sequence], output_dir, file_name):

    audio_objects = []
    video_objetcs = []

    for obj in objects:
        render_obj = obj.render()
        if isinstance(render_obj, mpe.VideoClip):
            video_objetcs.append(render_obj)
        elif isinstance(render_obj, mpe.AudioClip):
            audio_objects.append(render_obj)

    print(objects, video_objetcs, audio_objects)

    final_render: mpe.CompositeVideoClip = mpe.CompositeVideoClip(
        video_objetcs, bg_color=None)

    final_render = final_render.set_audio(
        mpe.CompositeAudioClip(audio_objects))

    final_render.write_videofile(
        os.path.normpath(Path(output_dir) / Path(f"{file_name}.mp4")), codec="libx264", threads=4, fps=24)
