import moviepy.editor as mpe
import os


class Sequence:

    def __init__(self, start_time, duration=None) -> None:
        self.start_time = 0
        self.duration = duration
        self.objects = []

    def stop_at(self, stop_time):
        self.duration = stop_time-self.start_time
        for index, obj in enumerate(self.objects):
            if isinstance(obj, mpe.VideoClip) or isinstance(obj, mpe.AudioClip):
                if obj.duration is None or obj.start+obj.duration > stop_time:
                    self.objects[index] = obj.set_duration(stop_time-obj.start)
                    print(obj.start,obj.duration,">",stop_time-obj.start)
            else:
                obj.stop_at(stop_time)


    def append_obj(self, obj):
        self.objects.append(obj)

    def render(self, output_path=None):
        audio_objects = []
        video_objects = []

        final_render = None

        def get_all_objects(obj):
            if isinstance(obj, Sequence):
                for o in obj.objects:
                    get_all_objects(o)
            else:
                if isinstance(obj, mpe.VideoClip):
                    video_objects.append(obj)
                elif isinstance(obj, mpe.AudioClip):
                    audio_objects.append(obj)

        get_all_objects(self)

        print(video_objects)

        match (len(video_objects) > 0, len(audio_objects) > 0):
            case False, False:
                final_render = None
            case False, True:
                final_render = mpe.CompositeAudioClip(audio_objects)
            case True, False:
                final_render = mpe.CompositeVideoClip(video_objects)
            case True, True:
                final_render = mpe.CompositeVideoClip(video_objects).set_audio(
                    mpe.CompositeAudioClip(audio_objects))

        if final_render:
            final_render = final_render.set_duration(self.duration)

        if output_path and final_render:
            final_render.write_videofile(os.path.normpath(output_path), codec="libx264", threads=4, fps=24)
        
        return final_render
