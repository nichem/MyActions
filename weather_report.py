import requests, os
from common import *

KEY = os.environ.get("WEATHER_KEY")


def getLocationId():
    location = "宝安区"
    url = f"https://geoapi.qweather.com/v2/city/lookup?location={location}&key={KEY}"
    html = requests.get(url)
    return html.json()["location"][0]["id"]


def getWeatherInfo():
    url = f"https://devapi.qweather.com/v7/weather/3d?location={getLocationId()}&key={KEY}"
    html = requests.get(url)
    json = html.json()
    day = json["daily"][0]
    return f"早间：{day['textDay']} 晚间：{day['textNight']} 温度：{day['tempMin']} ~ {day['tempMax']}"


if __name__ == "__main__":
    weather_info = getWeatherInfo()
    notify(weather_info, weather_info)
