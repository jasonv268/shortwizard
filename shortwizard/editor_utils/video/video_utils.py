import math
from PIL import Image
import numpy
from moviepy.editor import concatenate_videoclips, VideoFileClip, vfx, ImageSequenceClip
from skimage.filters import gaussian



def crop_bg(bg_clip):
    h_original = bg_clip.h

    w_edit = bg_clip.w*1920 / h_original

    bg_clip = bg_clip.resize((w_edit, 1920)).on_color(
        size=(1080, 1920), color=(0, 0, 0))

    return bg_clip


def resize(clip, w, h):
    
    clip.w = clip.w * w
    clip.h = clip.h * h

    return clip


def blur(clip, duration):
    def dynamic_blur(image, t):
        """ Returns a dynamically blurred version of the image """
        max_blur_radius = 50  # Rayon maximal de flou
        blur_radius = max_blur_radius * (1 - t / duration)  # Flou décroissant avec le temps
        # Assurez-vous que le flou tombe bien à 0 à la fin de la période de flou
        blur_radius = max(blur_radius, 0)
        # Interpolation gaussienne pour une transition plus douce
        return gaussian(image.astype(float), sigma=blur_radius)

    blur_clip = clip.subclip(0, duration)
    
    # Appliquer le flou dynamique à chaque trame de la période de flou
    blurred_frames = [dynamic_blur(frame, t) for t, frame in blur_clip.iter_frames(with_times=True)]
    blurred_clip = ImageSequenceClip(blurred_frames, fps=clip.fps)
    
    # Concaténer la vidéo floue avec la vidéo originale après la période de flou
    return concatenate_videoclips([blurred_clip, clip.set_start(duration)])



def zoom_in(clip, zoom_ratio=0.04):
    def effect(get_frame, t):
        img = Image.fromarray(get_frame(t))
        base_size = img.size

        new_size = [
            math.ceil(img.size[0] * (1 + (zoom_ratio * t))),
            math.ceil(img.size[1] * (1 + (zoom_ratio * t)))
        ]

        # The new dimensions must be even.
        new_size[0] = new_size[0] + (new_size[0] % 2)
        new_size[1] = new_size[1] + (new_size[1] % 2)

        img = img.resize(new_size, Image.LANCZOS)

        x = math.ceil((new_size[0] - base_size[0]) / 2)
        y = math.ceil((new_size[1] - base_size[1]) / 2)

        img = img.crop([
            x, y, new_size[0] - x, new_size[1] - y
        ]).resize(base_size, Image.LANCZOS)

        result = numpy.array(img)
        img.close()

        return result

    return clip.fl(effect)


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

def zoom(t, duration):
    # Starting scale factor
    start_scale = 1
    # End scale factor (the size to which the text should grow)
    end_scale = 1.2

    # Calculate the scaling factor based on elapsed time and total duration
    scale_factor = start_scale + min(t / duration, 1.0) * (end_scale - start_scale)

    return scale_factor




