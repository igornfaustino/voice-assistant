from __future__ import print_function
import datetime
import pickle
import pytz
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from common import utils
import pathlib

# PATHS
ROOT_PATH = utils.get_root_path()
PICKLE_PATH = pathlib.Path(ROOT_PATH).joinpath('token.pickle')
CREDENTIALS_PATH = pathlib.Path(ROOT_PATH).joinpath('credentials.json')

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june',
          'july', 'august', 'september', 'october', 'november', 'december']
DAYS = ['monday', 'tuesday', 'wednesday',
        'thursday', 'friday', 'saturday', 'sunday']
DAY_EXTENSIONS = ["nd", "rd", "th", "st"]


def auth():
    creds = None

    if os.path.exists(PICKLE_PATH):
        with open(PICKLE_PATH, 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_PATH, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(PICKLE_PATH, 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    return service


def _get_datetime_range(date) -> (datetime.datetime, datetime.datetime):
    start_date = datetime.datetime.combine(date, datetime.datetime.min.time())
    end_date = datetime.datetime.combine(date, datetime.datetime.max.time())
    utc = pytz.UTC
    start_date = start_date.astimezone(utc)
    end_date = end_date.astimezone(utc)

    return start_date, end_date


def get_events(service, date):
    start_date, end_date = _get_datetime_range(date)
    events_result = service.events().list(calendarId='primary',
                                          timeMin=start_date.isoformat(),
                                          timeMax=end_date.isoformat(),
                                          singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    return events


def _get_year(today: datetime.date, month: int) -> int:
    has_month = month != -1
    isMonthThisYear = today.month <= month
    if has_month and not isMonthThisYear:
        return today.year + 1
    return today.year


def _get_month(day: int):
    today = datetime.date.today()
    has_day = day != -1
    is_day_this_month = today.day <= day
    if (has_day and not is_day_this_month):
        return today.month + 1
    return today.month


def _get_day(day_of_week: int, is_next_date) -> datetime.date:
    today = datetime.date.today()
    current_day_of_week = today.weekday()
    dif = day_of_week - current_day_of_week
    is_next_week = dif < 0

    if is_next_week:
        dif += 7
    if is_next_date:
        dif += 7
    return today + datetime.timedelta(dif)


def _get_date_from_words(text: str) -> datetime.date:
    day = -1
    day_of_week = -1
    month = -1

    for word in text.split():
        if word in MONTHS:
            month = MONTHS.index(word) + 1
        elif word in DAYS:
            day_of_week = DAYS.index(word)
        elif word.isdigit():
            day = int(word)
        else:
            for ext in DAY_EXTENSIONS:
                found_ext = word.find(ext)
                if found_ext > 0:
                    try:
                        day = int(word[:found_ext])
                    except Exception:
                        pass

    has_day = day != -1
    has_day_of_week = day_of_week != -1
    has_month = month != -1
    is_next_date = text.count('next') >= 1

    if not has_day and has_day_of_week:
        return _get_day(day_of_week, is_next_date)
    if not has_month and has_day:
        month = _get_month(day)
    year = _get_year(datetime.date.today(), month)

    return datetime.date(year=year, month=month, day=day)


def get_date_from_text(text: str):
    lower_text = text.lower()

    if (lower_text.count('today') > 0):
        return datetime.date.today()

    return _get_date_from_words(lower_text)
