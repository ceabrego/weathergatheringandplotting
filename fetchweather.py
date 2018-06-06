# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 09:53:04 2018

@author: dscabrego
"""

from requests import get
import json
from pprint import pprint
#%%
url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/1648902'
weather = get(url).json()['items']
pprint(weather)

#%% Finding the distance between two points
#my location is 42.476735, -83.291542
