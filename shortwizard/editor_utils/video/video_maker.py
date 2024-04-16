from moviepy.editor import VideoFileClip, concatenate_videoclips

from shortwizard.editor_utils.Sequence import Sequence
from shortwizard.editor_utils.video import VideoBackgroundsManager
from shortwizard.editor_utils.video import video_utils
from shortwizard.editor_utils.video import Video
from shortwizard.editor_utils.img import image_utils


def create_video(video: 'Video.Video')->Sequence:

    sequence = Sequence(0)

    video_clip: VideoFileClip = VideoFileClip(video.file_path).set_start(0)

    if (video.basique.mask_color):
        video_clip = image_utils.remove_green_screen(video_clip, video.basique.mask_color)

    if(video.basique.opacity != 1.0):
        video_clip = video_clip.set_opacity(video.basique.opacity)

    if (video.basique.zoom != 1.0):
        video_clip = video_clip.resize(video.basique.zoom)

    if video.position[0] =="center":
        video.position = (540 - video_clip.size[0]//2, video.position[1])

    video_clip = video_clip.set_position(video.position)

    if (video.animation):
        if (video.animation.size_func):
            video_clip = video_clip.resize(video.animation.size_func)

        if (video.animation.position_func):

            position_fun = lambda t: video.animation.position_func(video.position[0], video.position[1], t)

            video_clip = video_clip.set_position(position_fun)

    
     


    sequence.objects = [video_clip]

    return sequence


def create_bg(vbm: VideoBackgroundsManager.VideoBackgroundsManager, short_duration):

    bg_clip = VideoFileClip(vbm.get_video_background_string_path())

    bg_clip = video_utils.crop_bg(bg_clip)

    bg_clip = video_utils.fade_in_out_bg(bg_clip)

    #bg_clip = video_utils.blur(bg_clip, 1)

    if bg_clip.duration > short_duration:
        bg_clip = bg_clip.subclip(0, short_duration)
        bg_clip = video_utils.fade_in_out_bg(bg_clip)
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

