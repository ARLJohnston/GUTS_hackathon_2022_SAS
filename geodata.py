import geopandas as gpd
import matplotlib as plt
import pandas as pd
import folium

from PIL import Image
from selenium import webdriver
import os
import time
import requests
from folium.plugins import HeatMap

BASE_URL = 'https://nominatim.openstreetmap.org/search?format=json'

postcode = 'G42 9AY'
response = requests.get(f"{BASE_URL}&postalcode={postcode}")
response = response.json()

latitude = response[0].get('lat')
longitude = response[0].get('lon')
loc = [latitude, longitude] 
OSmap = folium.Map(location = loc,
                   zoom_start=13,
                   tiles='openstreetmap')

OSmap.save("map.html")

def generate_map_image(x,y):
    temp = 'file://{path}/{mapfile}'.format(path=os.getcwd(),mapfile=x)
    browser = webdriver.Firefox()
    browser.get(temp)

    time.sleep(3)
    browser.save_screenshot(y)
    browser.quit()

def generate_heat_map(lat,long):
    geo_map = folium.Map(location=[lat,long],zoom_start=18)

    tmp_arr = []
    tmp_arr.append([lat,long])

    HeatMap(tmp_arr).add_to(geo_map)

    fname= 'heatmap.html'
    geo_map.save(fname)
    generate_map_image(fname,'heatmap.png')

generate_heat_map(latitude,longitude)