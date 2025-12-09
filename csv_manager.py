# Handles interaction with specification .csv files, including loading/saving and interface for CRUD 

import csv

CSV_FILE_PATH = 'data/specifications.csv'

# Load and return specifications csv file
def load_specs(filepath):
    specs = []
    with open(filepath, mode = 'r', newline = '', encoding = 'utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            specs.append(row)
    return specs

def display_specs(data):
    for row in data:
        print(row)