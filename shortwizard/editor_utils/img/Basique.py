from shortwizard.editor_utils.VideoSequence import VideoSequence
from moviepy.editor import VideoClip, VideoFileClip
from moviepy.editor import vfx

import copy


class Basique:

    def __init__(self, mask_color=None, has_mask=False, opacity=1.0, resize=1.0) -> None:
        self.mask_color = mask_color
        self.has_mask = has_mask
        self.opacity = opacity
        self.resize = resize
        self.sequence = VideoSequence(0)

    def link_sequence(self, sequence):
        self.sequence = sequence
        # basique_copy = copy.deepcopy(self)
        # basique_copy.sequence = sequence
        # return basique_copy

    def set_all(self):
        print("set all")
        print(self.sequence.objects)
        if self.mask_color is not None:
            print("mask color")
            self.set_mask_color(self.mask_color)
        if self.has_mask:
            print("has mask")
            self.set_has_mask(self.has_mask)
        if self.opacity != 1.0:
            self.set_opacity(self.opacity)
        if self.resize != 1.0:
            self.set_resize(self.resize)
        return self.sequence

    def set_mask_color(self, mask_color):

        self.mask_color = mask_color

        def set_mask_color_rec(sequence):
            for index, obj in enumerate(sequence.objects):
                if isinstance(obj, VideoFileClip):
                    sequence.objects[index] = obj.fx(
                        vfx.mask_color, color=self.mask_color, thr=150, s=100)
                elif isinstance(obj, VideoSequence):
                    set_mask_color_rec(obj)

        set_mask_color_rec(self.sequence)

        return self.sequence

    def set_has_mask(self, has_mask):

        self.has_mask = has_mask

        def set_has_mask_rec(sequence):
            for index, obj in enumerate(sequence.objects):
                if isinstance(obj, VideoFileClip):
                    sequence.objects[index] = VideoFileClip(obj.filename, has_mask=self.has_mask)
                elif isinstance(obj, VideoSequence):
                    print("rec has mask")
                    set_has_mask_rec(obj)

        print(self.sequence.objects)

        set_has_mask_rec(self.sequence)

        return self.sequence

    def set_opacity(self, opacity):

        self.opacity = opacity

        def set_opacity_rec(sequence):
            for index, obj in enumerate(sequence.objects):
                if isinstance(obj, VideoClip):
                    sequence.objects[index] = obj.set_opacity(self.opacity)
                elif isinstance(obj, VideoSequence):
                    set_opacity_rec(obj)

        set_opacity_rec(self.sequence)

        return self.sequence

    def set_resize(self, resize):

        self.resize = resize

        def set_zoom_rec(sequence):
            for index, obj in enumerate(sequence.objects):
                if isinstance(obj, VideoClip):

                    sequence.objects[index] = obj.resize(self.resize)

                elif isinstance(obj, VideoSequence):
                    set_zoom_rec(obj)

        set_zoom_rec(self.sequence)

        return self.sequence


default = Basique()
default_has_mask = Basique(has_mask=True)
