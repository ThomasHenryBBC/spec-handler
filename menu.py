# Handles the user interface and user inputs

def amend_spec_menu():
    while True:
        print("\nWhich specification would you like to amend: \n")
        print("1. Search by SpecID")
        print("2. Search by Name")
        print("3. Return to main menu")

        amend_choice = input("\nWhat would you like to do?: ").strip()
        if amend_choice not in ['1', '2', '3']:
            print("\nInvalid choice. Please enter a number 1 to 3.")

        print("\n--Fields--\n")
        print("1. specID")
        print("2. name")
        print("3. version")
        print("4. date finalised")
        print("5. description")
        print("6. screenshot URL")
        print("7. labelsAndValues")
        print("8. implementationStatusWeb")
        print("9. implementationStatusTV")
        print("10. implementationStatusIOS")
        print("11. implementationStatusAndroid")

        field_choice = input("\nWhich field would you like to amend: \n")
        if field_choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']:
            print("\nInvalid choice. Please enter a number 1 to 11.")

# TODO: Add validation for each field within validator.py
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

def delete_spec_menu():
    print("\n--Delete Specification--\n")
    print("1. Delete specification (search by specID)")
    print("2. Delete specification (search by name)")
    print("3. Return to main menu")

    delete_choice = input("\nWhat would you like to do?: ").strip()

    if delete_choice in ['1', '2', '3']:
        return delete_choice
    else:
        print("\nInvalid choice. Please enter a number 1 to 3.")

def display_single_spec_menu():
    while True:
        print("\n--Specification Search--\n")
        print("1. Search by SpecID")
        print("2. Search by Name")
        print("3. Return to main menu")

        display_single_spec_choice = input("\nWhat would you like to do?: ").strip()

        if display_single_spec_choice in ['1', '2', '3']:
            return display_single_spec_choice
        else:
            print("\nInvalid choice. Please enter a number 1 to 3.")

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
