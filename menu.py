# Handles the user interface

def show_menu():
    while True:
        print("\n--Specification Manager--\n")
        print("1. Display specifications")
        print("2. Add a new specification")
        print("3. Amend a specification")
        print("4. Delete a specification")
        print("5. Quit app\n")

        choice = input("\nWhat would you like to do?: ").strip()

        if choice in ['1', '2', '3', '4', '5']:
            return choice
        else:
            print("\nInvalid choice. Please enter a number 1 to 5.")

def create_spec_menu():
    fields = []
    print("\nThis will add a new specification to the csv file. Please enter data for each field.\n")
    fields.append(input("specID: "))
    fields.append(input("name: "))
    fields.append(input("version: "))
    fields.append(input("date finalised: "))
    fields.append(input("description: "))
    fields.append(input("screenshot URL: "))
    fields.append(input("labelsAndValues: "))
    fields.append(input("implementationStatusWeb: "))
    fields.append(input("implementationStatusTV: "))
    fields.append(input("implementationStatusIOS: "))
    fields.append(input("implementationStatusAndroid: "))
    return fields

def display_specs_menu():
    while True:
        print("\n--Display Specifications--\n")
        print("1. Display all specifications")
        print("2. Display single specification")
        print("3. Return to main menu")

        display_choice = input("\nWhat would you like to do?: ").strip()

        if display_choice in ['1', '2', '3']:
            return display_choice
        else:
            print("\nInvalid choice. Please enter a number 1 to 3.")

def display_single_spec_menu():
    while True:
        print("\n--Specification Search--\n")
        print("1. Search by SpecID")
        print("2. Search by Name")
        print("3. Return to main menu")

        display_single_spec_choice = input("\nWhat would you like to do?: ")

        if display_single_spec_choice in ['1', '2', '3']:
            return display_single_spec_choice
        else:
            print("\nInvalid choice. Please enter a number 1 to 3.")