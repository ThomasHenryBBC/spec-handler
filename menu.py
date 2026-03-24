# Handles the user interface and user inputs

from validator import validate_field

def amend_spec_menu():
    while True:
        print("\nWhich specification would you like to amend: ")
        print("1. Search by SpecID")
        print("2. Search by Name")
        print("3. Return to main menu")

        amend_choice = input("\nWhat would you like to do?: ").strip()

        # Exit early if user wants to go back
        if amend_choice == '3':
            return '3', None
        elif amend_choice == '1':
            search_input = input("\nEnter SpecID of specification to amend: ").strip()
            return amend_choice, search_input
        elif amend_choice == '2':
            search_input = input("\nEnter Name of specification to amend: ").strip().lower()
            return amend_choice, search_input
        else:
            print("\nInvalid choice. Please enter a number 1 to 3.")


def amend_field_menu():
    # Displays fields and gets input for new field value from user
    while True:    
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

        field_choice = input("\nWhich field would you like to amend (1-11): \n")

        if field_choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']:
            print("\nInvalid choice. Please enter a number 1 to 11.")
            continue

        field_index = int(field_choice) - 1 # Convert choice to corresponding field index value

        # Loop until user gives valid choice
        while True:
            # Ask for new value of amended field
            new_value = input("\nEnter the new value: ").strip()

            is_valid, error_msg = validate_field(field_index, new_value) # Check validity and get error message if invalid

            if is_valid:
                return field_choice, new_value
            else:
                print(f" Error. {error_msg}")


def create_spec_menu():
    fields = []
    field_names = [
        "SpecID", "name", "version", "date finalised (DD/MM/YYYY)", "description", "screenshot URL", "labelsAndValues", "implementationStatusWeb (TRUE/FALSE)", "implementationStatusTV (TRUE/FALSE)", "implementationStatusIOS (TRUE/FALSE)", "implementationStatusAndroid (TRUE/FALSE)"
    ]

    print("\nThis will add a new specification to the csv file. Please enter data for each field.\n")
    
    # Enumerate gives index and name of field
    for index, field_name in enumerate(field_names):
        while True:
            value = input(f"{field_name}: ").strip()

            is_valid, error_msg = validate_field(index, value) # Check validity and get error message if invalid

            if is_valid:
                fields.append(value)
                break
            else:
                print(f" Error. {error_msg}")

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

def get_confirmation(action):
    # Reusable function that asks user for a yes/no confirmation of action
    while True:
        choice = input(f"\nAre you sure you want to {action}? (Y/N): ").strip().upper()
        if choice == 'Y':
            return True
        elif choice == 'N':
            return False
        else:
            print("Invalid input. Please enter Y or N")