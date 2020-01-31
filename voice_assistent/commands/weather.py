import requests
from common.voice import speak
from common.utils import get_current_public_ip, send_notification
from common.config import GEOLOCATION_API_KEY, WEATHER_API


def get_geolocation():
    ip = get_current_public_ip()
    geolocation_info = requests.get(
        f"http://api.ipstack.com/{ip}?access_key={GEOLOCATION_API_KEY}"
    ).json()
    return geolocation_info


def get_weather():
    geolocation = get_geolocation()
    latitude = geolocation["latitude"]
    longitude = geolocation["longitude"]
    return requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&units=metric&lon={longitude}&APPID={WEATHER_API}").json()


def speak_weather():
    weather = get_weather()
    description = weather["weather"][0]["description"]
    temp = weather["main"]["temp"]
    send_notification(f"Temp: {temp}°C, Description: {description}")
    speak(
        f"today we have a {description} and we are at {temp} degrees celsius")
