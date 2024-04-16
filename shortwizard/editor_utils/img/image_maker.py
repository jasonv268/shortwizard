
from moviepy.editor import ImageClip

from shortwizard.editor_utils.Sequence import Sequence
from shortwizard.editor_utils.img import image, image_utils
from shortwizard.editor_utils.img.animation import Animation



def create_image(img: 'image.Image')->Sequence:
    sequence = Sequence(0)

    image_clip: ImageClip = ImageClip(img.file_path).set_start(0)
    image_clip = image_clip.set_position(img.position)

    if (img.basique.mask_color):
        image_clip = image_utils.remove_green_screen(image_clip, img.basique.mask_color)

    if(img.basique.opacity != 1.0):
        image_clip = image_clip.set_opacity(img.basique.opacity)

    if (img.basique.zoom != 1.0):
        image_clip = image_clip.resize(img.basique.zoom)

    if (img.animation):
        if (img.animation.size_func):
            image_clip = image_clip.resize(img.animation.size_func)

        if (img.animation.position_func):

            position_fun = lambda t: img.animation.position_func(img.position[0], img.position[1], t)

            image_clip = image_clip.set_position(position_fun)

    sequence.objects = [image_clip]

    return sequence