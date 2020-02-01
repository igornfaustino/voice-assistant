import os
import re
from common import voice


WEB_SUPORTED_APPS = {"notion": "notion.so", "habitica": "habitica.com"}


def handle_search(trigger, text):
    topic = re.search(f'.*{trigger} (a |the )?(.*)', text).group(2)
    voice.speak(f'Okay')
    search(topic)


def search(text: str):
    search_String = text.replace(' ', '+')
    os.system(f'x-www-browser "www.google.com/search?q={search_String}"')


def open_web_app(app):
    app_url = WEB_SUPORTED_APPS[app]
    os.system(f'x-www-browser "{app_url}"')


def handle_open(text: str):
    software = text.split("open")[-1].strip()
    if software in WEB_SUPORTED_APPS:
        return open_web_app(software)