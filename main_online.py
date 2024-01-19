import requests
import json
import datetime


def weather_for_city(city, api):
  url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + api
  response = requests.get(url)
  print (response.content)
  """
  data = json.loads(response.content)
  # raw data
  """
  weather_raw_tempature = data['main']['temp']
  weather_raw_feel_like = data['main']['feels_like']
  weather_raw_pressure = data['main']['pressure']
  weather_raw_tempature_min = data['main']['temp_min']
  weather_raw_tempature_max = data['main']['temp_max']
  weather_raw_humidity = data['main']['humidity']
  weather_raw_wind_speed = data['wind']['speed']
  weather_raw_sky_condition = data['weather'][0]['main']
  weather_raw_wind_deg = data['wind']['deg']
  weather_raw_wind_gust = data['wind']['gust']
  weather_raw_clouds = data['clouds']['all']
  # full data

  weather_full_city = '**Weather for {}**'.format(data['name'])
  weather_full_tempature = 'Temperature: {} degrees Celsius'.format(data['main']['temp'])
  weather_full_humidity = 'Humidity: {} %'.format(data['main']['humidity'])
  weather_full_wind_speed = 'Wind speed: {} m/s'.format(data['wind']['speed'])
  weather_full_sky_condition = 'Sky condition: {}'.format(data['weather'][0]['description'])

  print(weather_raw_tempature)
  print(weather_raw_feel_like)
  print(weather_raw_pressure)
  print(weather_raw_tempature_min)
  print(weather_raw_tempature_max)
  print(weather_raw_humidity)
  print(weather_raw_wind_speed)
  print(weather_raw_sky_condition)
  print(weather_raw_wind_deg)
  print(weather_raw_wind_gust)
  print(weather_raw_clouds)
  






weather_for_city("Berlin","4e4e25da3c76c95c7c348925a7e2310a")