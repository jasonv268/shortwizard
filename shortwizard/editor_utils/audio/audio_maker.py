from moviepy.editor import AudioFileClip
from shortwizard.editor_utils.Sequence import Sequence
from shortwizard.editor_utils.audio import audio


def create_audio(audio: 'audio.Audio')-> Sequence:

    sequence = Sequence(0)

    audio_clip: AudioFileClip = AudioFileClip(audio.file_path)

    if audio.basique:
        if audio.basique.volume:
            audio_clip = audio_clip.volumex(audio.basique.volume)

        if audio.basique.fade_in:
            audio_clip = audio_clip.audio_fadein(audio.basique.fade_in)
        
        if audio.basique.fade_out:
            audio_clip = audio_clip.audio_fadeout(audio.basique.fade_out)

    if audio.speed != 1:
        audio_clip = audio_clip.fx(audio.speedx, audio.speed)

    sequence.objects += [audio_clip]

    return sequence