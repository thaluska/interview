import pyowm
import os

#api_key = os.environ['OPENWEATHER_API_KEY']
#weather_location = os.environ['CITY_NAME']


try:

  os.environ['OPENWEATHER_API_KEY']
  os.environ['CITY_NAME']

except:
 
 print 'OPENWEATHER_API_KEY or CITY_NAME are not declared'

else:

  api_key = os.environ['OPENWEATHER_API_KEY']
  weather_location = os.environ['CITY_NAME']

  
  owm = pyowm.OWM(api_key)
  observation = owm.weather_at_place(weather_location)
  
  w = observation.get_weather()
  c = observation.get_location()
  
  city = c.get_name()
  
  temp = w.get_temperature('celsius')
  current_temp = temp['temp']
  current_weather = w.get_detailed_status()
  humidity = w.get_humidity()
  
  print 'source=openweathermap, city="%s", description="%s", temp=%.2f, humidity=%d' % (city, current_weather, current_temp, humidity)
