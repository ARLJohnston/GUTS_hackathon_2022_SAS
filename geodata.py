import geopandas as gpd
import matplotlib as plt
import pandas as pd
import pyepsg as pep
import folium as fl
import io
from PIL import Image
from selenium import webdriver
import os
import time
p_loc = pd.read_csv("location_data_2.csv",sep=',', on_bad_lines='warn',header=0,)

geometry = gpd.points_from_xy(p_loc.Longitude,p_loc.Latitude)

geo_loc = gpd.GeoDataFrame(p_loc,geometry=geometry)

map = fl.Map(location=[geo_loc['Latitude'][0],geo_loc['Longitude'][0]],tiles= "OpenStreetMap",zoom_start=18)

h_file = "map.html"

temp = 'file://{path}/{mapfile}'.format(path=os.getcwd(),mapfile=h_file)
browser = webdriver.Firefox()
browser.get(temp)

time.sleep(5)
browser.save_screenshot('map.png')
browser.quit()