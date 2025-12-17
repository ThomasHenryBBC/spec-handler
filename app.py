# Core application logic, imports functions to manage flow of program

import sys  # Allows use of sys.ext(), which is preferred over quit() to exit program
from csv_manager import load_specs, display_all_specs, display_single_spec, CSV_FILE_PATH
from menu import show_menu, display_specs_menu, display_single_spec_menu

# Entry point of spec handler app
def main():
    
    # Load specification csv
    csv = load_specs(CSV_FILE_PATH)

    # Display specs
    print('\n Specifications loaded:\n')
    display_all_specs(csv)

    while True:
        choice = show_menu()

        # Display specs
        if choice == '1':
            display_choice = display_specs_menu()

            if display_choice == '1':
                print("\nAll specifications:\n")
                display_all_specs(csv)

            elif display_choice == '2':
                display_single_spec_choice = display_single_spec_menu()         
                if display_single_spec_choice == '1':
                    search_input = input("\nEnter SpecID: ")
                    display_single_spec(csv, '1', search_input)
                elif display_single_spec_choice == '2':
                    search_input = input("\nEnter spec name: ").lower()
                    display_single_spec(csv, '2', search_input)
                else:
                    break

            else:
                break

        elif choice == '2':
            fields = []
            print("\nThis will add a new specification to the csv file. Please enter data for each field.")
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
            print(fields)
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        elif choice == '5':
            quit_program()


def quit_program():
    print("\nExiting specification handler. Goodbye!")
    sys.exit(0)
    
# Standard 'entry point' check to prevent running when imported elsewhere, e.g. when unit testing
if __name__ == '__main__':
    main()