import geopandas as gpd
import matplotlib as plt
import pandas as pd
import folium

from selenium import webdriver
import os
import time
import requests
from folium.plugins import HeatMap

import numpy as np
import data_collection as dc


def generate_map_object() -> None:
    # im sure i've mucked something up here, fix this if needed pls :)

    BASE_URL = 'https://nominatim.openstreetmap.org/search?format=json'

    postcode = 'G12 8QQ' #university postcode
    response = requests.get(f"{BASE_URL}&postalcode={postcode}")
    response = response.json()

    latitude = response[0].get('lat')
    longitude = response[0].get('lon')
    loc = [latitude, longitude] 
    OSmap = folium.Map(location = loc,
                       zoom_start=13,
                       tiles='openstreetmap')

    OSmap.save("map.html") 

    return (latitude,longitude)


def lat_long_by_time():
    """Get data based on time, to able to add variation to
    heat map colouring
    
    Should produce a numpy array or pandas dataframe, ideally the latter
    that looks something like [name,location] and by extension
    the coordinates of the person at that current time"""

    return None
def generate_map_image(x,y):
    temp = 'file://{path}/{mapfile}'.format(path=os.getcwd(),mapfile=x)
    browser = webdriver.Firefox()
    browser.get(temp)

    time.sleep(3)
    browser.save_screenshot(y)
    browser.quit()

def generate_heat_map(lat,long):
    """ Generates a heatmap depending on what coordinates it is fed,
    currently only does one at a time but the append line can be put
    in a loop to add all the available coordinates into the temp array
    and feed it into the HeatMap generation
    
    Refer to this if needed: https://bytescout.com/blog/plotting-geographical-heatmaps-using-python-folium-library.html
    """


    geo_map = folium.Map(location=[lat,long],zoom_start=18)

    tmp_arr = []
    tmp_arr.append([lat,long]) # edit this to accomodate an array

    HeatMap(tmp_arr).add_to(geo_map)

    fname= 'heatmap.html'
    geo_map.save(fname)

    generate_map_image(fname,'heatmap.png')

tup = generate_map_image

generate_heat_map(tup[0],tup[1])