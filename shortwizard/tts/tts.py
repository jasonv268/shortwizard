from gtts import gTTS
from pathlib import Path
from shortwizard.editor_utils.MyTextClip import TtsTextClip
from pydub import AudioSegment




def generate_voices(item_list: list[TtsTextClip], lang: str, output_dir: str):
    """Generate voices for the given text list."""
    for index, item in enumerate(item_list):
        tts = gTTS(text=item.get_text_content(), lang=lang, slow=False)
        tts_path = Path(output_dir) / f"{index}.mp3"
        item.set_tts_path(tts_path)
        tts.save(tts_path)

        # Charger le fichier audio
        audio = AudioSegment.from_mp3(tts_path)

        # Accélérer le son par un facteur de 1.1
        audio_accelere = audio.speedup(playback_speed=1.3)

        # Écraser le fichier audio original avec le fichier audio accéléré
        audio_accelere.export(tts_path, format="mp3")


def generate_voice(text, output_path):
    tts = gTTS(text=text, lang="fr", slow=False)
    tts.save(output_path)
    audio = AudioSegment.from_mp3(output_path)

    # Accélérer le son par un facteur de 1.1
    audio_accelere = audio.speedup(playback_speed=1.3)

    # Écraser le fichier audio original avec le fichier audio accéléré
    audio_accelere.export(output_path, format="mp3")