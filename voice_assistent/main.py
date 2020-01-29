import commands
from common import voice
from pocketsphinx import LiveSpeech


def listen_to_wakeup(wakeup_command):
    speech = LiveSpeech(lm=False, keyphrase=wakeup_command,
                        kws_threshold=1e-20)
    for phrase in speech:
        print("oi")
        commands.handler(voice.get_audio_input())


if __name__ == '__main__':
    listen_to_wakeup('alfred')
    # commands.handler("am i busy")
