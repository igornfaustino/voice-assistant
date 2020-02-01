from newsapi import NewsApiClient
from common import voice
from common.utils import send_notification

# Init
newsapi = NewsApiClient(api_key='5dc834a547c240b4970b41323a193965')


def get_top_headlines():
    return newsapi.get_top_headlines(language='en',
                                     country='br', page_size=10)['articles']


def handle_news():
    voice.speak("playing the brazilian news now")
    headlines = get_top_headlines()
    for headline in headlines:
        send_notification(headline['title'])
        voice.speak(headline['title'], lang="pt-br")
