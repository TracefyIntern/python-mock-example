import os

import requests
from dotenv import load_dotenv

load_dotenv()


def meme(int, int2):
    return int + int2 + 2


def get_weather(latitude, longitude):
    api_key = os.getenv('WEATHER_API_KEY')
    api_url_base = os.getenv('WEATHER_API_URL', 'http://dataservice.accuweather.com')
    api_url = f'{api_url_base}/locations/v1/cities/geoposition/search'

    params = {
        'apikey': api_key,
        'q': f'{latitude},{longitude}'
    }

    response = requests.get(api_url, params=params)
    print(api_url)

    if response.status_code == 200:
        location_data = response.json()
        location_key = location_data['Key']

        api_url = f'{api_url_base}/currentconditions/v1/{location_key}'

        params = {
            'apikey': api_key,
        }

        print(api_url)
        return requests.get(api_url, params=params)


if __name__ == '__main__':
    weather = get_weather(52.180303, 4.456705)
    print(weather.json())
