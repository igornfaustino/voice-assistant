import commands
from common import voice
from pocketsphinx import LiveSpeech


def listen_to_wakeup(wakeup_command):
    speech = LiveSpeech(lm=False, keyphrase=wakeup_command,
                        kws_threshold=1e-15)
    for phrase in speech:
        commands.handler(voice.get_audio_input())


if __name__ == '__main__':
    listen_to_wakeup('oracle')
    # commands.handler("bootstrap protocol")
