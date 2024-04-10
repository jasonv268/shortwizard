from moviepy.editor import AudioFileClip

def create_audio(path, max_duration: int):

    audio_clip = AudioFileClip(path)

    if audio_clip.duration > max_duration:
        audio_clip = audio_clip.subclip(0, max_duration)

    return audio_clip


def fade_in_out_audio(audio_clip, fadein_duration=2, fadeout_duration=2):
    # Appliquer un fondu en entrée
    audio_fadein = audio_clip.audio_fadein(fadein_duration)

    # Appliquer un fondu en sortie
    audio_fadeout = audio_fadein.audio_fadeout(fadeout_duration)

    return audio_fadeout