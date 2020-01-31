import playsound
import speech_recognition as sr
from .utils import create_audio_file


def speak(text, lang="en"):
    filename = create_audio_file(text, lang)
    playsound.playsound(filename, block=True)


def get_audio_input() -> str:
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        # recognizer.adjust_for_ambient_noise(source, duration=0.5)
        # speak('yes')
        audio = recognizer.listen(source, phrase_time_limit=5)
    said = ''

    try:
        said = recognizer.recognize_google(audio)
        print(said)
    except Exception as ex:
        print(f"Exception: {str(ex)}")

    return said.lower()
