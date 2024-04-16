from moviepy.editor import vfx


def remove_green_screen(clip, mask_color=(0, 255, 0)):

    transparent_clip = clip.fx(
        vfx.mask_color, color=mask_color, thr=150, s=100)
    transparent_clip.set_opacity(0.8)

    return transparent_clip