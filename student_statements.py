import numpy as np
import pandas as pd

import data_collection


def generate_students():

    student_data = []
    with open('student_statements.txt') as l:
        data = l.readlines()
        for line in data:
            line = line[:-1]

        i = 0
        for j in range(int(len(data)/5) + 1):
            indiv_student = {}
            student_id = data[i+1].split(": ")
            name = data[i+2].split(": ")
            testimony = data[i+3].split(": ")

            indiv_student.update({student_id[0]: student_id[1][:-1],
                                 name[0]: name[1][:-1],
                                 testimony[0]: testimony[1][:-1]})
            student_data.append(indiv_student)

            i += 5

    return_data = np.array(student_data)
    return return_data

def gather_student_statement_locations():
    l = data_collection.get_location_location()
    locations = l['Location'].to_list()
    student_data = generate_students()

    print(locations)

    formatted_locations = []
    for location in locations:
        formatted_locations.append(location.lower())

    student_statement_data = []

    for data in generate_students():
        student_id = data['Student Number']
        student_locations = []
        data['Testimony'] = data['Testimony'].lower()
        for location in formatted_locations:
            if location in data['Testimony']:
                student_locations.append(location)
        if 'qmu' in data['Testimony']:
            student_locations.append("queen margaret union")
        if 'the union' in data['Testimony']:
            student_locations.append("glasgow university union")
        if 'the boyd orr' in data['Testimony']:
            student_locations.append("boyd orr Building")
        if 'the boydy' in data['Testimony']:
            student_locations.append("boyd orr building")
        if 'the park' in data['Testimony']:
            student_locations.append("kelvingrove park")
        if 'kg' in data['Testimony']:
            student_locations.append('kelvingrove park')
        if 'to kelvingrove' in data['Testimony']:
            student_locations.append('kelvingrove park')
        if 'the medicine building' in data['Testimony']:
            student_locations.append('wolfson medical building')
        if 'the wolfson' in data['Testimony']:
            student_locations.append('wolfson medical building')
        if 'kelvin grove' in data['Testimony']:
            student_locations.append('Kelvingrove Park')
        if 'guu' in data['Testimony']:
            student_locations.append('glasgow university union')
        if 'the adam smith' in data['Testimony']:
            student_locations.append('adam smith building')

            #REMOVE 'WHAT IN THE BOYD ORR'
            #REMOVE 'TAKE OUT THE BOYD ORR'
            #IF THE SAME PLACE COMES UP TWICE IN A ROW, REMOVE THE SECOND

        student_statement_data.append({student_id : student_locations})

    print(student_statement_data)
    return student_statement_data

def format_locations(locations):
    for i in range(len(locations)):
        if locations[i] == locations[i+1]:
            locations.remove(list[i+1])

def get_location_list(student_id):
    if type(student_id) == dict:
        key = list(student_id.keys())
        return student_id.get(key[0])
    return student_id

data = gather_student_statement_locations()

