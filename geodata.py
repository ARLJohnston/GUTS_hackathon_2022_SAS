import geopandas as gpd
import matplotlib as plt
import pandas as pd
import folium
import io
from PIL import Image
from selenium import webdriver
import os
import time
import requests

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

h_file = "map.html"

temp = 'file://{path}/{mapfile}'.format(path=os.getcwd(),mapfile=h_file)
browser = webdriver.Firefox()
browser.get(temp)

time.sleep(5)
browser.save_screenshot('map.png')
browser.quit()
