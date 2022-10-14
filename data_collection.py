import pandas as pd
import numpy as np


# Load the three data files for use in later functions
location_data = pd.read_csv("location_data.csv", on_bad_lines='warn')
people_data = pd.read_csv("people_data.csv", on_bad_lines='warn')
security_data = pd.read_csv("security_logs.csv", on_bad_lines='warn')

# Helper Functions regarding location data

# Location Data row getters
# returns all datasets as NumPy arrays
def get_building_names():
    return location_data['Building Name'].to_numpy()

def get_geolocations():
    return location_data['Geolocation'].to_numpy()

def get_opening_times():
    return location_data['Opening Times'].to_numpy()

def get_description():
    return location_data['Description'].to_numpy()

b = get_building_names()
g = get_geolocations()
o = get_opening_times()
d = get_description()

