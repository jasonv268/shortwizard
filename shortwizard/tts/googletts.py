import os
from pathlib import Path
from google.cloud import texttospeech

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'test_service_account.json'

client = texttospeech.TextToSpeechClient()


def generate_voice(text_content, output_path):
    """Generate voice for the given text content."""

    voice = texttospeech.VoiceSelectionParams(
        language_code="fr-CA",
        name="fr-CA-Neural2-B",
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        effects_profile_id=["small-bluetooth-speaker-class-device"],
        speaking_rate=0.9,
        pitch=1,
    )

    synthesis_input = texttospeech.SynthesisInput(text=text_content)

    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    with open(output_path, 'wb') as audio_file:
        audio_file.write(
            response.audio_content
        )

def generate_voices(item_list, lang: str, output_dir: str):
    """Generate voices for the given text list."""

    voice = texttospeech.VoiceSelectionParams(
        language_code="fr-CA",
        name="fr-CA-Neural2-B",
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        effects_profile_id=["small-bluetooth-speaker-class-device"],
        speaking_rate=0.9,
        pitch=1,
    )

    for index, item in enumerate(item_list):
        tts_path = Path(output_dir) / f"{index}.mp3"
        item.set_tts_path(tts_path)

        text_block = item.get_text_content()

        synthesis_input = texttospeech.SynthesisInput(text=text_block)

        response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
        )

        with open(tts_path, 'wb') as audio_file:
            audio_file.write(
                response.audio_content
                )