from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx, CompositeVideoClip

from shortwizard.editor_utils.Sequence import Sequence
from shortwizard.editor_utils.video import VideoBackgroundsManager
from shortwizard.editor_utils.video import video_utils
from shortwizard.editor_utils.video import Video
from shortwizard.editor_utils.img import image_utils

from shortwizard.config import root_assets


def create_bg(vbm: VideoBackgroundsManager.VideoBackgroundsManager, short_duration):

    bg_clip = VideoFileClip(vbm.get_video_background_string_path())

    bg_clip = video_utils.crop_bg(bg_clip)

    bg_clip = video_utils.fade_in_out_bg(bg_clip)


    rush_effect = VideoFileClip(
        root_assets / "video" / "fire.mp4").set_opacity(0.7)

    rush_effect = image_utils.remove_green_screen(rush_effect, (0, 255, 0))

    bg_clip = CompositeVideoClip([bg_clip, rush_effect.set_position("center")])

    if bg_clip.duration > short_duration:
        bg_clip = bg_clip.subclip(0, short_duration)
        bg_clip = video_utils.fade_in_out_bg(bg_clip)

    else:
        while bg_clip.duration < short_duration:
            bg_aux = VideoFileClip(vbm.get_video_background_string_path())
            if bg_aux.duration > short_duration - bg_clip.duration:
                bg_aux_duration = short_duration - bg_clip.duration
                if bg_aux_duration < 2:
                    bg_aux_duration = 2
                bg_aux = bg_aux.subclip(0, bg_aux_duration)
            bg_aux = video_utils.crop_bg(bg_aux)
            bg_aux = video_utils.fade_in_out_bg(bg_aux)
            bg_clip = concatenate_videoclips([bg_clip, bg_aux])

    bg_clip = bg_clip.without_audio()

    return bg_clip
