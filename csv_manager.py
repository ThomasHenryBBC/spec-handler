# Handles CRUD interactions with specification .csv file

import csv  # python module to handle csv files

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
    # Read csv file to memory as list, delete spec
    specs = []
    with open(filepath, 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            specs.append(row)
            if delete_by == '1': # search by specID and delete
                if search_input == row[0]:
                    specs.remove(row)
            elif delete_by == '2': # search by spec name and delete
                if search_input == row[1].lower():
                    specs.remove(row)
            else:
                print("ERROR: Can only search by specID or name\n")

    # Write updated spec list to csv
    with open(filepath, 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(specs)
