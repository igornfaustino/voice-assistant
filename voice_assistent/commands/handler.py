from . import date, applications
from common.voice import speak
from learning import intents

intent_predictor = intents.Intents()
intent_predictor.train()


def handler(text):
    if not text:
        return

    intent = intent_predictor.predict(text)
    print(intent)
    if not intent:
        return speak(text)
    if intent == "check_calendar":
        return date.handle_check_plans(text)
    if intent == "search":
        return speak("search")
