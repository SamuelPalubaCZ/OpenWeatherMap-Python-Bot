"""
  print('**Weather for {}**'.format(data['name']))
  print('Temperature:', data['main']['temp'], 'degrees Celsius')
  print('Humidity:', data['main']['humidity'], '%')
  print('Wind speed:', data['wind']['speed'], 'm/s')
  print('Sky condition:', data['weather'][0]['description'])
"""
weather.locate("json.json")