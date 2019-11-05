import re
import dateutil.parser
from timefhuman import timefhuman

from common import voice
from common import google_calendar

service = google_calendar.auth()


def handle_check_plans(text):
    normalized_text = re.sub(r'(\d+)(th|st|nd|rd)', r'\g<1>', text)
    date = timefhuman(normalized_text)
    events = google_calendar.get_events(service, date)
    _speakEvents(events)


def _speakEvents(events):
    if not events:
        return voice.speak('No upcoming events found')

    if (len(events) == 1):
        voice.speak(f'You have {len(events)} event')
    else:
        voice.speak(f'You have {len(events)} events')
    for event in events:
        event_datetime = dateutil.parser.parse(
            event['start'].get('dateTime', event['start'].get('date')))
        start_time = event_datetime.hour
        time_period = 'am'
        if start_time > 12:
            start_time -= 12
            time_period = 'pm'
        event_desc = event['summary']
        voice.speak(f'{event_desc} at {start_time} {time_period}')
