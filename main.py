import requests
import json



#url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + api
#print(url)
#response = requests.get(url)
def uloz(city, api, soubor="data.json"):
  url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + api
  response = requests.get(url)
  with open("data.json", "w") as data:
    data.write(response.text)


def nacti(soubor="data.json"):
  with open(soubor) as data:
    return data.read()
#print(nacti())



def precti(info):
  data = json.loads(nacti())
  #raw data
  weather_raw_city = data['name']
  weather_raw_humidity = data['main']['humidity']
  weather_raw_tempature = data['main']['temp']
  weather_raw_wind_speed = data['wind']['speed']
  weather_raw_sky_condition = data['weather'][0]['description']
  #full data
  weather_full_city = '**Weather for {}**'.format(data['name'])
  weather_full_tempature = 'Temperature: ' + str(data['main']['temp']) + ' degrees Celsius'
  weather_full_humidity = 'Humidity: ' + str(data['main']['humidity']) + '%'
  weather_full_wind_speed = 'Wind speed: ' + str(data['wind']['speed']) + ' m/s'
  weather_full_sky_condition = 'Sky condition: ' + (data['weather'])[0]['description']
  if info == "raw":
    print()
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
    

precti("raw")
precti("full")