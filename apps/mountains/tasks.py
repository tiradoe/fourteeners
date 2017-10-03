from __future__ import absolute_import

import urllib.request
import json
import time

from celery.task.schedules import crontab
from celery.decorators import periodic_task
from apps.mountains.models import Mountain, Weather
from django.conf import settings


@periodic_task(run_every=(crontab(hour="*", minute="*", day_of_week="*")))
def update_weather():
    mountains = Mountain.objects.all()
    for mountain in mountains:
        weather = get_weather(mountain, 'today')
        forecast = Weather.objects.create(
            mountain = mountain,
            day = 1,
            county = weather['name'],
            status = weather['desc'],
            image = weather['image'],
            speed = weather['wind_speed'],
            temp = weather['temp'],
            cloud = weather['clouds'],
            humidity = weather['humidity'],
        )
        forecast.save()
        print('done')


def get_weather(mountain, day='today'):
    name = mountain.name
    latitude = str(mountain.lat)
    longitude = str(mountain.long)
    count = '7' if day == 'week' else '2'
    position = 0 if day == 'today' else 1
    units = 'imperial'
    stats = {}

    url = 'http://api.openweathermap.org/data/2.5/forecast/daily?'
    query_string = (
                    'lat=' + latitude +
                    '&lon=' + longitude +
                    '&cnt=' + count +
                    '&units=' + units +
                    '&APPID=' + settings.WEATHER_API_KEY +
                    '&mode=json'
                    )

    try:
        weather_data = urllib.request.urlopen(url + query_string, timeout=5).readall().decode('utf-8')
    except urllib.error.URLError as e:
        print(url + query_string)
        print(e)
        stats = {
                    'name': 'DATA UNAVAILABLE',
                    'image': '',
                    'desc': 'DATA UNAVAILABLE',
                    'wind_speed': 0,
                    'temp': 0,
                    'clouds': 0,
                    'humidity':0,
                }
        return stats

    weather_json = json.loads(weather_data)
    weather_info = weather_json['list'][position]

    stats['name'] = weather_json['city']['name']
    stats['image'] = (
                        "http://openweathermap.org/img/w/" +
                        weather_info['weather'][0]['icon'] +
                        '.png'
                    )
    stats['desc'] = weather_info['weather'][0]['description']
    stats['wind_speed'] = weather_info['speed']
    stats['temp'] = weather_info['temp']['day']
    stats['clouds'] = weather_info['clouds']
    stats['humidity'] = weather_info['humidity']

    return stats
