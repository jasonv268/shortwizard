from gtts import gTTS
from pathlib import Path
from shortwizard.utils.Item import Item



def generate_voices(item_list: list[Item], lang: str, output_dir: str):
    """Generate voices for the given text list."""
    for index, item in enumerate(item_list):
        tts = gTTS(text=item.get_text_content(), lang=lang, slow=False)
        tts_path = Path(output_dir) / f"{index}.mp3"
        item.set_tts_path(tts_path)
        tts.save(tts_path)