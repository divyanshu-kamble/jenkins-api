import json
import requests

# Base_url = "http://api.openweathermap.org/data/3.0/onecall/timemachine?"
#
#
#
# lat="39.099724"
# lon = "-94.578331"
# dt= "1643803200"
#
# https://archive-api.open-meteo.com/v1/archive?latitude=51.51&longitude=-0.13&start_date=2022-12-20&end_date=2023-01-23&hourly=apparent_temperature&daily=apparent_temperature_max&timezone=Asia%2FSingapore&temperature_unit=fahrenheit&windspeed_unit=ms

url1 = "https://archive-api.open-meteo.com/v1/archive?latitude=52.52&longitude=13.41&start_date=2022-12-20&end_date=2023-01-19&hourly=temperature_2m"


response = requests.get(url1).json()

print(response)

s = json.dumps(response)
open("/Users/dkamble.intern/Documents/jenkins-data/weather.json","w").write(s)
