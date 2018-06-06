# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 10:29:59 2018
fetching local weather
@author: dscabrego
"""
from requests import get
import json
from pprint import pprint
from haversine import haversine
#%%
stations = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'
weather = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/'

my_lat = 42.476735
my_lon = -83.291542

all_stations = get(stations).json()['items']
#%%
def find_closest():
    smallest = 20036
    for n in all_stations:
        station_lon = n['weather_stn_long']
        station_lat = n['weather_stn_lat']
        distance = haversine(my_lon, my_lat, station_lon, station_lat)
        #print(distance)
        
        if distance < smallest:
            smallest = distance
            closest_station = n['weather_stn_id']
            closest_station_name = n['weather_stn_name']
    return closest_station
    #return closest_station_name, closest_station, smallest  

closest_stn = find_closest()

weather  = weather + str(closest_stn)
my_weather = get(weather).json()['items']
pprint(my_weather)
# the closest weather station is 9821383