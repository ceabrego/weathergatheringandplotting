# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from requests import get
import json
import folium
import os
import webbrowser
import html
#%%
url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'

stations = get(url).json()
lons = [n['weather_stn_long'] for n in stations['items']]
lats = [n['weather_stn_lat'] for n in stations['items']]
wsnames = [n['weather_stn_name'] for n in stations['items']]
#wsnames = [html.escape(n['weather_stn_name']) for n in stations['items']]
#%% setting up your map
#map_ws = folium.Map(location=[0,0], zoom_start=1)
map_ws = folium.Map(location=[0,0],zoom_start=2)

CWD = os.getcwd()

for n in range(len(lons)):
    folium.Marker([lats[n], lons[n]], popup=wsnames[n], icon = folium.Icon(icon='cloud', color='green')).add_to(map_ws)

map_ws.save('wsmap1.html')
webbrowser.open_new('file://'+CWD+'/'+'wsmap1.html')