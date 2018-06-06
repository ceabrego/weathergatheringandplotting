# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 11:14:40 2018
plotting weather
@author: dscabrego
"""
from requests import get
import matplotlib.pyplot as plt 
from dateutil import parser

url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallmeasurements/9821383'
weather = get(url).json()

# =============================================================================
# temperatures=[]
# for n in weather['items']:
#     temperature = n['ambient_temp']
#     temperatures.append(temperature)
# =============================================================================

temperatures  = [n['ambient_temp'] for n in weather['items']]
time_stamps = [parser.parse(n['reading_timestamp']) for n in weather['items']]
#%%
plt.plot(time_stamps,temperatures)
plt.xlabel('Time')
plt.ylabel('Temperature, C')
plt.show
