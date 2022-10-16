
from calendar import c
import pandas as pd
import numpy as np
from certifi import where

# Load the three data files for use in later functions
location_data = pd.read_csv("location_data.csv", on_bad_lines='warn')
people_data = pd.read_csv("people_data.csv", on_bad_lines='warn')
security_data = pd.read_csv("security_logs.csv", on_bad_lines='warn')
lecture_data = pd.read_csv("lecture_timing.csv", on_bad_lines='warn')

main_data = security_data.merge(people_data, on=['Student ID'])
location_data.rename(columns={'Building Name': 'Location'}, inplace=True)
main_data = main_data.merge(location_data, on=['Location'])
main_data.to_csv('main.csv')


# Helper Functions regarding location data

# Location Data row getters
# returns all datasets as NumPy arrays
def get_location_location():
    location_formatted = []
    dat = location_data['Location'].to_numpy()
    for value in dat:
        location_formatted.append(value.lower())
    df = pd.DataFrame(dat, columns=['Location'])
    return df


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

# Function which splits location_data's geolocation into a latitude and longitude
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

def get_students_under_age(age, location):
    frame = people_data[['Student ID','Age']].to_numpy()
    under_18s = frame[frame[:,1]<age,0]
    sussy_students = security_data[security_data['Student ID'].isin(under_18s)]
    sussy_students = sussy_students.loc[sussy_students['Location'] == location]
    print(sussy_students)
    return sussy_students
    

# A function which takes a student ID, and outputs every location and time recorded
def get_locations_and_times(student_id):
    instances = []

    for index, row in main_data.iterrows():
        if row['Student ID'] == student_id:
            instances.append([row['Location'], row['Time']])

    if len(instances) == 0:
        return None

    return_array = np.array(instances)
    return return_array


# Function that returns a dictionary containing a student ID, and a list of all their
# locations based on the security logs
def get_locations_as_dict(student_id):
    instances = []

    for index, row in main_data.iterrows():
        if row['Student ID'] == student_id:
            instances.append(row['Location'])

    if len(instances) == 0:
        return None

    dictionary = {student_id : instances}
    return dictionary


# A function which returns a boolean based on whether a student's timed locations has no contradictions
def times_match(student_id):
    case = get_locations_and_times(student_id)
    if type(case) is None:
        return None
    times = case[:, 1]

    time_list = []
    for time in times:
        time_split = time.split('-')
        time_list.append(time_split)

    time_list.sort(key=lambda row: (int(row[0])))
    print(time_list)
    for time in time_list:
        while time[0][0] == '0':
            time[0] = time[0][1:]
        while time[1][0] == '0':
            time[1] = time[1][1:]

    for i in range(len(time_list) - 1):
        if int(time_list[i][1]) > int(time_list[i + 1][0]):
            return False

    return True

# Function which gets a
def get_point_time(time):
    student_times = security_data.copy()
    student_times[['Start', 'End']] = student_times['Time'].str.split('-', 1, expand=True).to_numpy()
    student_times = student_times.drop('Time', axis=1)
    student_times['Start'] = student_times['Start'].astype(int)
    student_times['End'] = student_times['End'].astype(int)

    student_times_array = student_times.to_numpy()
    # print(student_times_array)
    next_day_mask = np.array(student_times_array[:, 3] > student_times_array[:, 4])
    student_times_array[next_day_mask, 4] += 2400
    #print(student_times_array.shape)
    # student_times_array[:,4] = dc.np.where(,student_times_array[:,4],student_times_array[:,4]+2400)

    mask = np.where((student_times_array[:, 3] < time) & (student_times_array[:, 4] > time))

    return student_times_array[mask]


def get_building_loc(name):
    loc = location_data.to_numpy()
    loc = loc[loc[:,0]==name,1]
    if len(loc) == 0:
        return None
        
    return [float(i) for i in loc[0][1:-2].split(' ')]

def get_bld_name(lat,long):
    a = latitude_longitude().to_numpy()
    name = ""
    for i in range(len(a)):
        if (float(a[i][4]) == lat) & (float(a[i][5]) == long):
            name = a[i][0]
    
    return name
                
def get_bld_desc(name):
    a = latitude_longitude().to_numpy()
    desc = ""
    for i in range(len(a)):
        if a[i][0]==name:
            desc = a[i][3]
    return desc

       
def get_student_locations(time):
    present = get_point_time(time)
    person_geoloc = pd.DataFrame(columns = ["building","latitude", "longitude", "color", "size","time"])
    #print(present)
   
    was_breaked = False
    for i in present:
        geo = get_building_loc(i[2])
        
        if geo is None:
            was_breaked = True
            break
        
        
        person_geoloc.loc[len(person_geoloc.index)] = [i[2],geo[0], geo[1], 1, 10,time]

    

    groupped_person = person_geoloc.groupby(['building','latitude', 'longitude']).size().reset_index()
    
    groupped_person.columns = ['building','latitude', 'longitude', 'size']
  
    groupped_person['size'] = groupped_person['size'].apply(lambda x: x)
    groupped_person['color'] = 1
    groupped_person['time'] = time
    
    columns_titles = ["building","latitude", "longitude", "color", "size","time"]
    groupped_person=groupped_person.reindex(columns=columns_titles)
    
    return groupped_person

def slider_wrapper(time):
    hours = (time // 100)*100
    minutes = ((60/100)*(time % 100))//1
    return get_student_locations(hours+minutes)

def get_operating_time():
    loc = location_data.copy()
    loc[['Open', 'Close']] = location_data['Opening Times'].str.split('-', 1, expand=True).to_numpy()
    loc['Open'] = loc['Open'].astype(int)
    loc['Close'] = loc['Close'].astype(int)
    next_day_mask = (loc['Open'] > loc['Close'])
    
    z_valid = loc[next_day_mask]

    
    loc.loc[next_day_mask, 'Close'] = z_valid['Close'] + 2400
    
    loc = loc.drop('Opening Times',axis=1)
    return loc
    

def check_out_of_working_hours():
    
    loc = get_operating_time()

    student_times = get_time_leaving()
    main_df = pd.merge(student_times, loc, on="Location", how="left")
    main_df['Start'] = main_df['Start'].astype(int)
    main_df['End'] = main_df['End'].astype(int)

    mask = ((main_df['Start'] >= main_df['Open']).astype(bool) & (main_df['Close'] >= main_df['End']).astype(bool))
    frames = [loc,student_times]
    result = pd.concat(frames)
    main_df = main_df.mask(mask).dropna()
    main_df = main_df[main_df['Location'] != 'Kelvingrove Park']
    return main_df


def get_overlap(student_id):
    case = get_locations_and_times(student_id)
    if case is None:
        return None
    times = case[:, 1]

    time_list = []
    for time in times:
        time_split = time.split('-')
        time_list.append(time_split)

    time_list.sort(key=lambda row: (int(row[0])))
    #print(time_list)
    entries = []
    leaves = []
    for i in time_list:
        entries.append(int(i[0]))
        leaves.append(int(i[1]))
    last_left = 0
    for i in range(len(entries)):
        if entries[i] < last_left:
          
            return True
        last_left = leaves[i]
def get_time_leaving():
    student_times = security_data.copy()
    student_times[['Start', 'End']] = student_times['Time'].str.split('-', 1, expand=True).to_numpy()
    student_times = student_times.drop('Time', axis=1)
    return student_times
    
def get_sus_people():

    sus_set = dict()
    for i in enumerate(people_data['Student ID']):
        
        if get_overlap(i[1]):
            if(i[1] not in sus_set):
                sus_set[i[1]] = 0
            sus_set[i[1]] += 1
            
    new_sus = check_out_of_working_hours()['Student ID']
    for i in new_sus:
        print('helooooo',i)
        if(i not in sus_set):
            sus_set[i] = 0
        sus_set[i] += 1

    new_new_sus = get_lecture()
    #print(new_new_sus)
    for i in enumerate(new_new_sus['Student ID']):
        
        print('heyyy!!!!',i)
        if(i[1] not in sus_set):
            sus_set[i[1]] = 0
        sus_set[i[1]] += 1
    return sus_set

def get_lecture():

    lecture_data['Start'] = lecture_data['Start'].astype(int)
    lecture_data['End'] = lecture_data['End'].astype(int)
    
    #print(lecture_data)

    student_times = get_time_leaving()
    
    main_df = pd.merge(student_times, lecture_data, on="Location", how="left")
    main_df = pd.merge(main_df,people_data, on="Student ID", how="left")
    main_df = main_df.dropna()


    main_df = main_df[main_df['Lecture'] != None]
    main_df['Start_x'] = main_df['Start_x'].astype(int)
    main_df['End_x'] = main_df['End_x'].astype(int)
    main_df['Start_y'] = main_df['Start_y'].astype(int)
    main_df['End_y'] = main_df['End_y'].astype(int)

 
 

    mask = (((main_df['Start_x'] <= main_df['Start_y']).astype(bool) & (main_df['End_x'] <= main_df['End_y']).astype(bool)) |((main_df['Start_x'] >= main_df['Start_y']).astype(bool) & (main_df['End_x'] >= main_df['End_y']).astype(bool)))
    mask2 = ((main_df['Subject'] == main_df['Lecture']).astype(bool))
    main_df = main_df.mask(mask).dropna()
    main_df = main_df.mask(mask2).dropna()
    #main_df = main_df.groupby('Student ID').size()
    #print(main_df[['Start_x','End_x','Start_y','End_y','Student ID','Lecture']])
    return main_df
    
def get_sus_mask():
    sus = get_sus_people()
    sus_mask = security_data['Student ID'].isin(sus.keys())
    
    return [security_data[~sus_mask], security_data[sus_mask]]


   


if __name__ == "__main__":
   #tests
    #print(get_sus_people())
    #get_lecture()
    print(get_sus_mask())

get_student_locations(1030)
