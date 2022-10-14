import pandas as pd
import numpy as np


# Load the three data files for use in later functions
location_data = pd.read_csv("location_data.csv", on_bad_lines='warn')
people_data = pd.read_csv("people_data.csv", on_bad_lines='warn')
security_data = pd.read_csv("security_logs.csv", on_bad_lines='warn')

# Helper Functions regarding location data

# Location Data row getters
# returns all datasets as NumPy arrays
def get_location_building_names():
    return location_data['Building Name'].to_numpy()

def get_location_geolocations():
    return location_data['Geolocation'].to_numpy()

def get_location_opening_times():
    return location_data['Opening Times'].to_numpy()

def get_location_description():
    return location_data['Description'].to_numpy()


# Getter functions for the attributes in people data
def get_people_student_id():
    return people_data['Student ID'].to_numpy()

def get_people_name():
    return people_data['Name'].to_numpy()
def get_people_age():
    return people_data['Age'].to_numpy()

def get_people_sex():
    return people_data['Sex'].to_numpy()

def get_people_year_of_study():
    return people_data['Year of Study'].to_numpy()

def get_people_subject():
    return people_data['Subject'].to_numpy()

def get_people_height():
    return people_data['Height'].to_numpy()

def get_people_hair_colour():
    return people_data['Hair colour'].to_numpy()

def get_people_societies():
    return people_data['Societies'].to_numpy()




