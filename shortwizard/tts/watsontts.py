import os
from pathlib import Path

from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator



#API
url = 'https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/04783d13-baf7-4d2a-9737-5f42ac2d8e76'

# Load API key from environment variable
apikey = "mBKXPi3jVRvs-9UZ8ufZLVLWs7ZXmMVMQICtb5EziRAZ"

# Setup Service
authenticator = IAMAuthenticator(apikey)
tts = TextToSpeechV1(authenticator=authenticator)
tts.set_service_url(url)

def generate_voices(item_list, lang: str, output_dir: str):
    """Generate voices for the given text list."""
    for index, item in enumerate(item_list):
        tts_path = Path(output_dir) / f"{index}.mp3"
        item.set_tts_path(tts_path)

        with open(tts_path, 'wb') as audio_file:
            audio_file.write(
                tts.synthesize(
                    item.get_text_content(),
                    voice='fr-FR_NicolasV3Voice',
                    accept='audio/mp3'
                ).get_result().content)