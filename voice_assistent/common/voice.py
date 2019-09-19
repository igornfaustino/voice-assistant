import playsound
import speech_recognition as sr
from .utils import create_audio_file


def speak(text):
    filename = create_audio_file(text)
    playsound.playsound(filename, block=True)


def get_audio_input() -> str:
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    said = ''

    try:
        said = recognizer.recognize_google(audio)
        print(said)
    except Exception as ex:
        print(f"Exception: {str(ex)}")

    return said.lower()
