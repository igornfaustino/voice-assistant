from __future__ import print_function
import datetime
import pickle
import os.path
from dateutil import tz
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
    utc = tz.tzlocal()
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
