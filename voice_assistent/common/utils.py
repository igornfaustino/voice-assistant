import os
from gtts import gTTS
from pathlib import Path
import notify2


filename = 'voice.mp3'
notify2.init("voice_assistant")


def create_audio_file(text, lang="en"):
    tts = gTTS(text, lang=lang)
    tts.save(filename)
    return filename


def get_root_path():
    return Path(__file__).parent.parent.parent


def open_page(link):
    def open_link(*args):
        print(link)
        os.system(
            f'x-www-browser "{link}"')

    return open_link


def send_notification(title, link=None):
    notification = notify2.Notification(title, link)
    notification.show()
