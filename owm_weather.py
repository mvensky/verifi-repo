#!/usr/bin/env python
# This from http://bigl.es/using-python-to-get-weather-data/
# This is version 1.0 of the code; absolute bare minimum requirements are to get LA weather
# from https://home.openweathermap.org and print it out
# Programmer: Michael J Vensky; date = 3-June-2017

import pyowm

city = "Los Angeles"
owm = pyowm.OWM('f1317d5040c0840a2ed62035447f0dd4')
observation = owm.weather_at_place(city)
w = observation.get_weather() 

print "For %s at %s GMT " % (city, w.get_reference_time('iso') )
print "The percentage cloud cover is %d" % w.get_clouds()
print "The humidity is %d%%" % w.get_humidity()
print "The pressure is %d mmHg" % w.get_pressure()['press']
print "The temperature is %.1f" % w.get_temperature('fahrenheit')['temp']
print "The expected maximum is %.1f" % w.get_temperature('fahrenheit')['temp_max']
print "The expected minimum is %.1f" % w.get_temperature('fahrenheit')['temp_min']
print "The wind speed is %.1f mph"  % (w.get_wind()['speed'])
