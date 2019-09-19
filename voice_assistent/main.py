import commands
from common import voice

if __name__ == '__main__':
    while(True):
        commands.handler(voice.get_audio_input())
