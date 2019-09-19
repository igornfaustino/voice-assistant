from . import date, applications
from common.voice import speak

CHECK_CALENDAR_TRIGGERS = [
    'do i have plans',
    'what do i have',
    'am i busy',
]

SEARCH_TRIGGERS = [
    'search for',
]


def handler(text):
    if not text:
        return

    for trigger in CHECK_CALENDAR_TRIGGERS:
        if trigger in text:
            return date.handle_check_plans(text)

    for trigger in SEARCH_TRIGGERS:
        if trigger in text:
            return applications.handle_search(trigger, text)
    speak(text)
