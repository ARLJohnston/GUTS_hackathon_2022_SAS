import pandas as pd
import numpy as np


# Load the three data files for use in later functions
location_data = pd.read_csv("location_data.csv", on_bad_lines='warn')
people_data = pd.read_csv("people_data.csv", on_bad_lines='warn')
security_data = pd.read_csv("security_logs.csv", on_bad_lines='warn')

main_data = security_data.merge(people_data, on=['Student ID'])
location_data.rename(columns={'Building Name':'Location'}, inplace=True)
main_data = main_data.merge(location_data, on=['Location'])
main_data.to_csv('main.csv')


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


# Getter functions for the attributes in security_logs
def get_security_student_id():
    return security_data['Student ID'].to_numpy()

def get_security_name():
    return security_data['Name'].to_numpy()

def get_security_location():
    return security_data['Location'].to_numpy()

def get_security_time():
    return security_data['Time'].to_numpy()

# Further Helper Functions
def latitude_longitude():
    locations = get_location_geolocations()
    i = 0
    list_convertion = []
    for item in locations:
        item = item[1:-1:]
        items = item.split(" ")
        for num in items:
            num = float(num)
        temp = np.asarray(items)
        list_convertion.append(temp)

    np_array = np.array(list_convertion)
    df = pd.DataFrame(np_array, columns=['Latitude', 'Longitude'])

    copy_of_location_data = location_data.copy()
    copy_of_location_data.drop('Geolocation', axis=1)

    result = pd.concat([copy_of_location_data, df], axis=1, ignore_index=False)
    return result