import commands
import playsound
from common import voice
from pocketsphinx import LiveSpeech


def listen_to_wakeup(wakeup_command):
    speech = LiveSpeech(lm=False, keyphrase=wakeup_command)
    for phrase in speech:
        playsound.playsound("listening.mp3")
        commands.handler(voice.get_audio_input())


if __name__ == '__main__':
    listen_to_wakeup('oracle')
    # commands.handler("How is the weather?")
