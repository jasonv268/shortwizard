from gtts import gTTS
from pathlib import Path
from shortwizard.utils.Item import Item
from pydub import AudioSegment




def generate_voices(item_list: list[Item], lang: str, output_dir: str):
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