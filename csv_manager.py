# Handles interaction with specification .csv files, including loading/saving and interface for CRUD 

import csv  # built in python module to handle csv files

CSV_FILE_PATH = 'spec-handler/data/specifications.csv'

# Load and return specifications csv file
def load_specs(filepath):
    specs = []
    with open(filepath, mode = 'r', newline = '', encoding = 'utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            specs.append(row)
    return specs

def display_all_specs(data):
    for row in data:
        print(row)

# def display_single_spec(data, search_by, search_input):
#   if search_by == 1:
#       for row in data: