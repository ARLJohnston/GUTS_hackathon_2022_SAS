import geopandas as gpd
import matplotlib as plt
import pandas as pd
import pyepsg as pep
import folium as fl

p_loc = pd.read_csv("location_data_2.csv",sep=',', on_bad_lines='warn',header=0,)

geometry = gpd.points_from_xy(p_loc.Longitude,p_loc.Latitude)

geo_loc = gpd.GeoDataFrame(p_loc,geometry=geometry)

#map = fl.Map(location=[geo_loc['Longitude'],geo_loc['Latitude']],tiles= "OpenStreetMap",zoom_start=12)
