from moviepy.editor import VideoFileClip, concatenate_videoclips

from shortwizard.editor_utils.video import VideoBackgroundsManager
from shortwizard.editor_utils.video import video_utils


def create_bg(vbm: VideoBackgroundsManager.VideoBackgroundsManager, short_duration):

    bg_clip = VideoFileClip(vbm.get_video_background_string_path())

    bg_clip = video_utils.crop_bg(bg_clip)

    #bg_clip = video_utils.fade_in_out_bg(bg_clip)

    bg_clip = video_utils.blur(bg_clip, 1)

    if bg_clip.duration > short_duration:
        bg_clip = bg_clip.subclip(0, short_duration)
        #bg_clip = video_utils.fade_in_out_bg(bg_clip)
        #bg_clip = video_utils.blur(bg_clip, 1)

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

    return bg_clip