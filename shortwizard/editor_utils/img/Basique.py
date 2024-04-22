from shortwizard.editor_utils.Sequence import Sequence
from moviepy.editor import VideoClip


class Basique:
    def __init__(self, mask_color=None, has_mask=False, opacity=1.0, zoom=1.0) -> None:
        self.mask_color = mask_color
        self.has_mask = has_mask
        self.opacity = opacity
        self.zoom = zoom

    def set_opacity(self, sequence, opacity=None):

        if opacity:
            self.opacity = opacity

        def set_opacity_rec(sequence):
            for index, obj in enumerate(sequence.objects):
                if isinstance(obj, VideoClip):
                    sequence.objects[index] = obj.set_opacity(self.opacity)
                elif isinstance(obj, Sequence):
                    set_opacity_rec(obj)

        if self.opacity != 1.0:
            set_opacity_rec(sequence)

        return self

    def set_zoom(self, sequence, zoom=None):

        if zoom:
            self.zoom = zoom

        def set_zoom_rec(sequence):
            for index, obj in enumerate(sequence.objects):
                if isinstance(obj, VideoClip):
                    
                    sequence.objects[index] = obj.resize(self.zoom)

                elif isinstance(obj, Sequence):
                    set_zoom_rec(obj)

        if self.zoom != 1.0:
            set_zoom_rec(sequence)

        return self


default = Basique()
default_has_mask = Basique(has_mask=True)
