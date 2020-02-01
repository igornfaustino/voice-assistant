import os
from .applications import handle_open
from .weather import speak_weather
from .news import handle_news
from .date import handle_check_plans
from common.voice import speak, get_audio_input


def bootstrap_protocol():
    speak("hi, activating bootstrap protocol")
    speak("opening your sites")
    handle_open("open notion")
    handle_open("open habitica")
    speak("consulting your daily informations")
    handle_check_plans("today")
    speak_weather()
    handle_news()


def audio_confirmation() -> bool:
    confirmation_code = get_audio_input()
    if confirmation_code == "000":
        return True
    return False


def knightfall_protocol():
    speak('knightfall protocol requires a voice code')
    if audio_confirmation():
        speak("activating knightfall protocol")
        speak('good night')
        return os.system('systemctl poweroff')
    speak('Voice code denied, aborting activation of knightfall protocol')


AVALIABLE_PROTOCOLS = {"bootstrap": bootstrap_protocol,
                       "knightfall": knightfall_protocol}


def handle_protocol(text):
    for protocol in AVALIABLE_PROTOCOLS.keys():
        if protocol in text:
            return AVALIABLE_PROTOCOLS[protocol]()
