import requests
import json


def weather_for_city(city,api, info="full"):
  #url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + api
  #print(url)
  #response = requests.get(url)
  def nacti():
    with open("data.json") as data:
      return data.read()
  #print(nacti())

  
  data = json.loads(nacti())
  #raw data
  weather_raw_city = data['name']
  weather_raw_tempature = data['main']['temp']
  weather_raw_humidity = data['main']['humidity']
  weather_raw_wind_speed = data['wind']['speed']
  weather_raw_sky_condition = data['weather'][0]['description']
  #full data
  weather_full_city = '**Weather for {}**'.format(data['name'])
  weather_full_tempature = 'Temperature:', data['main']['temp'], 'degrees Celsius'
  weather_full_humidity = 'Humidity:', data['main']['humidity'], '%'
  weather_full_wind_speed = 'Wind speed:', data['wind']['speed'], 'm/s'
  weather_full_sky_condition = 'Sky condition:', data['weather'][0]['description']

if info == "raw":
  print(weather_raw_tempature)
  print(weather_raw_humidity)
  print(weather_raw_wind_speed)
  print(weather_raw_sky_condition)
  print(weather_raw_city)
elif info == "full":
  print(weather_full_city)
  print(weather_full_tempature)
  print(weather_full_humidity)
  print(weather_full_wind_speed)
  print(weather_full_sky_condition)
    




weather_for_city("Berlin","4e4e25da3c76c95c7c348925a7e2310a")