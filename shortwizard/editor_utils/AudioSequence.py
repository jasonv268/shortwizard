from shortwizard.editor_utils.Sequence import Sequence
from moviepy.editor import AudioClip


class AudioSequence(Sequence):

    def __init__(self, start) -> None:
        super().__init__(start)


    def set_volume(self, volume):
        for index, obj in enumerate(self.objects):
            if isinstance(obj, AudioClip):
                self.objects[index] = obj.volumex(volume)
            elif isinstance(obj, AudioSequence):
                obj.set_volume(volume)
        return self