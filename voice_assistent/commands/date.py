import datetime
from common import voice
from common import google_calendar

service = google_calendar.auth()


def handle_check_plans(text):
    date = google_calendar.get_date_from_text(text)
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
        event_datetime = datetime.datetime.fromisoformat(
            event['start'].get('dateTime', event['start'].get('date')))
        start_time = event_datetime.hour
        time_period = 'am'
        if start_time > 12:
            start_time -= 12
            time_period = 'pm'
        event_desc = event['summary']
        voice.speak(f'{event_desc} at {start_time} {time_period}')
