from shortwizard.utils.Item import Item
import moviepy.editor as mpe
from shortwizard.utils import editor_assets, VideoBackgroundsManager, AudioBackgroundsManager
import os
from pathlib import Path

from shortwizard.config import root


def create_audio_and_text(item_list: list[Item], abm: AudioBackgroundsManager.AudioBackgroundsManager):

    audio_clip = mpe.AudioFileClip(abm.get_audio_background_path())

    audio_clip = audio_clip.volumex(0.1)

    time = 1

    video_clip_list = []

    for item in item_list:
        audio_part = mpe.AudioFileClip(item.get_tts_path())
        audio_part = audio_part.set_start(time)

        sound_effects = []

        if item.has_effects():

            effects = item.get_effects()

            audio_effects_clip, video_effects_clip = editor_assets.create_effects(
                effects, time, audio_part.duration)

            sound_effects += audio_effects_clip

            video_clip_list += video_effects_clip

        audio_clip = mpe.CompositeAudioClip(
            [audio_clip, audio_part]+sound_effects)

        video_clip_list += editor_assets.create_text_clip_list(
            item.get_text_content(), item.get_position(), time, time+audio_part.duration+item.get_pause_duration(), item.get_font_size(), item.get_chars_per_line())

        time = time + audio_part.duration + item.get_pause_duration()

    audio_clip = audio_clip.subclip(0, time)
    audio_clip = editor_assets.fade_in_out_audio(audio_clip)

    return audio_clip, video_clip_list


def create_bg(vbm: VideoBackgroundsManager.VideoBackgoundsManager, short_duration):

    bg_clip = mpe.VideoFileClip(vbm.get_video_background_string_path())

    bg_clip = editor_assets.crop_bg(bg_clip)

    bg_clip = editor_assets.fade_in_out_bg(bg_clip)

    if bg_clip.duration > short_duration:
        bg_clip = bg_clip.subclip(0, short_duration)
        bg_clip = editor_assets.fade_in_out_bg(bg_clip)

    else:
        while bg_clip.duration < short_duration:
            bg_aux = mpe.VideoFileClip(vbm.get_video_background_string_path())
            if bg_aux.duration > short_duration - bg_clip.duration:
                bg_aux_duration = short_duration - bg_clip.duration
                if bg_aux_duration < 3:
                    bg_aux_duration = 3
                bg_aux = bg_aux.subclip(0, bg_aux_duration)
            bg_aux = editor_assets.crop_bg(bg_aux)
            bg_aux = editor_assets.fade_in_out_bg(bg_aux)
            bg_clip = mpe.concatenate_videoclips([bg_clip, bg_aux])

    return bg_clip


def write_final_render(bg_clip, text_clip_list, audio_clip, output_dir, file_name):

    final_render = mpe.CompositeVideoClip(
        [bg_clip]+text_clip_list, bg_color=None).set_audio(audio_clip)

    final_render.write_videofile(
        os.path.normpath(Path(output_dir) / Path(f"{file_name}.mp4")), codec="libx264", fps=24)
