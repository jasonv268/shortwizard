from moviepy.editor import concatenate_videoclips, VideoFileClip, vfx
from shortwizard.editor_utils import Effect

def crop_bg(bg_clip):
    h_original = bg_clip.h

    w_edit = bg_clip.w*1920 / h_original

    bg_clip = bg_clip.resize((w_edit, 1920)).on_color(
        size=(1080, 1920), color=(0, 0, 0))

    return bg_clip


def fade_in_out_bg(bg_clip):
    # Fondu en entrée (fade in)
    fondu_clip_in = bg_clip.subclip(0, 0.5)
    fondu_fade_in = fondu_clip_in.fadein(0.5)

    # Fondu en sortie (fade out)
    fondu_clip_out = bg_clip.subclip(
        bg_clip.duration - 0.5, bg_clip.duration)
    fondu_fade_out = fondu_clip_out.fadeout(0.5)

    # Composition du fondu d'entrée et de sortie avec la vidéo de fond
    bg_clip = concatenate_videoclips([
        fondu_fade_in,
        bg_clip.subclip(0.5, bg_clip.duration - 0.5),
        fondu_fade_out
    ])

    return bg_clip

def resize(t, duration):
    # Starting scale factor
    start_scale = 1
    # End scale factor (the size to which the text should grow)
    end_scale = 1.2

    # Calculate the scaling factor based on elapsed time and total duration
    scale_factor = start_scale + min(t / duration, 1.0) * (end_scale - start_scale)

    return scale_factor


def edit_anim(path, start_time, end_time):
    follow_clip = VideoFileClip(path)

    follow_anim = follow_clip.subclip(start_time, end_time)
    follow_anim = follow_anim.resize((640, 360))
    follow_anim = follow_anim.set_position(("center", 200))
    follow_anim = follow_anim.fx(
        vfx.mask_color, color=(95, 206, 29), thr=100, s=100)
    follow_anim = follow_anim.fx(vfx.speedx, 1.5)
    follow_anim.set_opacity(0.8)

    return follow_anim


def create_anim(path, start_time, end_time, position):
    anim = VideoFileClip(path)

    anim = anim.subclip(start_time, end_time)
    # anim = anim.resize((640, 360))
    anim = anim.set_position(position)
    anim = anim.fx(
        vfx.mask_color, color=(1, 255, 11), thr=100, s=100)
    anim = anim.fx(vfx.speedx, 1.5)
    anim.set_opacity(0.8)

    return anim


def remove_green_screen(clip, effect: Effect.VideoEffect):

    anim = clip.fx(
        vfx.mask_color, color=effect.get_mask_color(), thr=100, s=100)
    anim.set_opacity(0.8)
    anim = anim.resize((640, 360))
    anim = anim.set_position(effect.get_position())

    return anim