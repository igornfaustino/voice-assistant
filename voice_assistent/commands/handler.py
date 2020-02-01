from . import date, applications, news, weather, protocol
from common.voice import speak
from learning import intents

intent_predictor = intents.Intents()
intent_predictor.train()


def handler(text):
    if not text:
        return

    intent = intent_predictor.predict(text)
    print(intent)
    try:
        if not intent:
            return speak(text)
        if intent == "check_calendar":
            return date.handle_check_plans(text)
        if intent == "search":
            return speak("search")
        if intent == "news":
            news.handle_news()
        if intent == "weather":
            weather.speak_weather()
        if intent == "open":
            applications.handle_open(text)
        if intent == "protocol":
            protocol.handle_protocol(text)
    except Exception as e:
        print(e)
        speak("Sorry, I can't understand you")
