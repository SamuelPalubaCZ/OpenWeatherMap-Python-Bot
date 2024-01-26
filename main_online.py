import requests
import json
import datetime
import requests
import json
import datetime


"""def weather_for_city(city, api):
  url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + api
  response = requests.get(url)
 
  print(response.content) """
def weather_for_city(city, api, file, format="utf-8"):
  url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + api
  response = requests.get(url)
  #data_format = json.dump(data, indent=2)
  
  # Save response.content to a text file
  with open(file, 'w') as file:
    file.write(response.content.decode(format))
    
    data = json.loads(response.content)




  
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
  
  # Generate weather_full_* variables
  weather_full_tempature = 'Temperature: {} degrees Celsius'.format(weather_raw_tempature)
  weather_full_feel_like = 'Feels Like: {} degrees Celsius'.format(weather_raw_feel_like)
  weather_full_pressure = 'Pressure: {} hPa'.format(weather_raw_pressure)
  weather_full_tempature_min = 'Min Temperature: {} degrees Celsius'.format(weather_raw_tempature_min)
  weather_full_tempature_max = 'Max Temperature: {} degrees Celsius'.format(weather_raw_tempature_max)
  weather_full_humidity = 'Humidity: {} %'.format(weather_raw_humidity)
  weather_full_wind_speed = 'Wind Speed: {} m/s'.format(weather_raw_wind_speed)
  weather_full_sky_condition = 'Sky Condition: {}'.format(weather_raw_sky_condition)
  weather_full_wind_deg = 'Wind Degree: {}'.format(weather_raw_wind_deg)
  weather_full_wind_gust = 'Wind Gust: {}'.format(weather_raw_wind_gust)
  weather_full_clouds = 'Clouds: {} %'.format(weather_raw_clouds)
  
  # Print weather_full_* variables
  print(weather_full_tempature)
  print(weather_full_feel_like)
  print(weather_full_pressure)
  print(weather_full_tempature_min)
  print(weather_full_tempature_max)
  print(weather_full_humidity)
  print(weather_full_wind_speed)
  print(weather_full_sky_condition)
  print(weather_full_wind_deg)
  print(weather_full_wind_gust)
  print(weather_full_clouds)


  
"""
  weather_full_city = '**Weather for {}**'.format(data['name'])
  weather_full_tempature = 'Temperature: {} degrees Celsius'.format(data['main']['temp'])
  weather_full_humidity = 'Humidity: {} %'.format(data['main']['humidity'])
  weather_full_wind_speed = 'Wind speed: {} m/s'.format(data['wind']['speed'])
  weather_full_sky_condition = 'Sky condition: {}'.format(data['weather'][0]['description'])
"""




weather_for_city("Berlin","4e4e25da3c76c95c7c348925a7e2310a", "json.json")