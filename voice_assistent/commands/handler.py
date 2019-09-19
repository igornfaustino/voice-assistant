from . import date
from common.voice import speak

CHECK_CALENDAR_TRIGGERS = [
    'do i have plans',
    'what do i have',
    'am i busy',
]


def handler(text):
    if not text:
        return

    for trigger in CHECK_CALENDAR_TRIGGERS:
        if trigger in text:
            return date.handle_check_plans(text)
    speak(text)
