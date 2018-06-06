# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 15:54:24 2018

@author: dscabrego
"""

from requests import get
import webbrowser
import folium
import os
import html

def colorgrad(minimum,maximum,value):
    minimum = float(minimum)
    maximum = float(maximum)
    ratio = 2 * (value - minimum)/(maximum-minimum)
    b = int(max(0,255*(1-ratio)))
    g = int(max(0,255*(ratio-1)))
    r = 255 - b - g
    hexcolor = '#%02x%02x%02x' % (r,g,b)
    return hexcolor
    
#%%
url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getalllastmeasurement'

station_data = get(url).json()

temps=[]
tmax=0
tmin=100
lons = [n['weather_stn_long'] for n in station_data['items']]
lats = [n['weather_stn_lat'] for n in station_data['items']]
wsnames = [html.escape(n['weather_stn_name']) for n in station_data['items']]

for n in station_data['items']:
    if 'ambient_temp' in n:
        t=n['ambient_temp']
        if t>50 or t<-30:
            t=20
        if t>tmax:
            tmax=t
        if t<tmin:
            tmin=t
        temps.append(t)

#temps = str(temps)
#%%
map_ws = folium.Map(location=[0,0], zoom_start=2)
for n in range(len(lons)-1):
    hcol = colorgrad(tmin,tmax,float(temps[n]))
    folium.CircleMarker([lats[n], lons[n]],
                        radius=5, 
                        popup=wsnames[n]+':'+str(temps[n]),
                        fill_color = hcol).add_to(map_ws)
    
CWD = os.getcwd()
map_ws.save('osm.html')
webbrowser.open_new_tab('file://'+CWD+'/'+'osm.html')
