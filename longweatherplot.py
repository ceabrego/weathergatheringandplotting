# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 11:57:17 2018
fetching a longer time history of weather data
@author: dscabrego
"""

from requests import get
import matplotlib.pyplot as plt 
from dateutil import parser

url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallmeasurements/9821383'
weather = get(url).json()

data = weather['items']
#weather2 = get(weather['next']['$ref']).json()
pages = 1
while 'next' in weather and pages < 5:
    url = weather['next']['$ref']
    print('Fetching {0}'.format(url))
    weather = get(url).json()
    data += weather['items']
    pages += 1
    
temperatures = [n['ambient_temp'] for n in data]
humidity_hist = [n['humidity'] for n in data]
time_stamp = [ parser.parse(n['reading_timestamp']) for n in data]


plt.plot(time_stamp, temperatures)
plt.plot(time_stamp, humidity_hist)
plt.xlabel('Time')
plt.ylabel('Temperature, C')
#plt.ylabel('humidity')
plt.show