from gtts import gTTS
from pathlib import Path

filename = 'voice.mp3'


def create_audio_file(text):
    tts = gTTS(text, lang='en')
    tts.save(filename)
    return filename


def get_root_path():
    return Path(__file__).parent.parent.parent
