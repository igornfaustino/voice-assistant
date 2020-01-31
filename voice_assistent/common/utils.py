import os
import notify2
import requests
from gtts import gTTS
from pathlib import Path


filename = 'voice.mp3'
notify2.init("voice_assistant")


def get_current_public_ip():
    return requests.get('https://api.ipify.org').text


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


def send_notification(title):
    notification = notify2.Notification(title)
    notification.show()
