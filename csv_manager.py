# Handles CRUD interactions with specification .csv file

import csv  # built in python module to handle csv files

CSV_FILE_PATH = 'data/specifications.csv'

def load_specs(filepath):
    specs = []
    # open csv file as readable
    with open(filepath, mode = 'r', newline='', encoding = 'utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            specs.append(row)
    return specs

def display_all_specs(data):
    for row in data:
        print(row)

def display_single_spec(data, search_by, search_input):
    if search_by == '1': # search by specID
        print(data[0])
        for row in data:
            if search_input == row[0]:
                print(row)
    elif search_by == '2': # search by spec name
        print(data[0])
        for row in data:
            if search_input == row[1].lower():
                print(row)
    else:
        print("ERROR: Can only search by specID or name\n")

def create_new_spec(filepath, fields):
    specs = load_specs(filepath)
    # open csv file as writeable
    with open(filepath, 'w', newline='') as file:
         writer = csv.writer(file)
         for row in specs:
             writer.writerow(row)
         writer.writerow(fields)

def delete_spec(filepath, delete_by, search_input):
    input = open(filepath, 'rb')
    output = open(filepath, 'wb')
    writer = csv.writer(input)
    if delete_by == '1': # search by specID and delete
        for row in csv.reader(input):
            if search_input != row[0]:
                writer.writerow(row)
    elif delete_by == '2': # search by spec name and delete
        for row in csv.reader(input):
            if search_input != row[1].lower():
                writer.writerow(row)
    else:
        print("ERROR: Can only search by specID or name\n")
    input.close()
    output.close()