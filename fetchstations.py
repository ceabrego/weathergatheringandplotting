# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from requests import get
import json
from pprint import pprint
#%%
url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'
stations = get(url).json()['items']
pprint(stations)
#colegio la salle (portugal) - 8477363