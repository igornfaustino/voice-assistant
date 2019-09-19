import os
import re
from common import voice


def handle_search(trigger, text):
    topic = re.search(f'.*{trigger} (a |the )?(.*)', text).group(2)
    voice.speak(f'Okay')
    search(topic)


def search(text: str):
    search_String = text.replace(' ', '+')
    os.system(f'x-www-browser "www.google.com/search?q={search_String}"')
