from os import environ

import requests

from . import WEATHER_URI


def city_lookup(city_name, api_key=environ['API_KEY']):
    return requests.get(f'{WEATHER_URI}?q={city_name}&appid={api_key}').json()


def zip_cc_lookup(zip_code, country_code, api_key=environ['API_KEY']):
    return requests.get(f'{WEATHER_URI}?zip={zip_code},{country_code}&appid={api_key}').json()


def lat_lon_lookup(lat, lon, api_key=environ['API_KEY']):
    return requests.get(f'{WEATHER_URI}?lat={lat}&lon={lon}&appid={api_key}').json()
