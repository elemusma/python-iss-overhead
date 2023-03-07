import requests
from datetime import datetime

MY_LAT = 39.739235
MY_LNG = -104.990250

parameters = {
    'lat': MY_LAT,
    'lng': MY_LNG,
    'formatted': 0
}

# response = requests.get(url='http://api.open-notify.org/iss-now.json')
response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)

response.raise_for_status()

data = response.json()

sunrise = data['results']['sunrise']
sunset = data['results']['sunset']

# longitude = data['iss_position']['longitude']
# latitude = data['iss_position']['latitude']

# iss_position = (longitude, latitude)

time_now = datetime.now()

sunrise = sunrise.split('T')[1].split(':')[0]
sunset = sunset.split('T')[1].split(':')[0]
print(sunrise)
print(sunset)
print(time_now.hour)

# 1XX: HOLD ON
# 2XX: HERE YOU GO
# 3XX: GO AWAY
# 4XX: YOU SCREWED UP
# 5XX: I SCREWED UP