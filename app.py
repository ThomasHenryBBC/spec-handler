# Core application logic, imports functions to manage flow of program

import sys  # Allows use of sys.ext(), which is preferred over quit() to exit program
from csv_manager import create_new_spec, delete_spec, load_specs, display_all_specs, display_single_spec, CSV_FILE_PATH
from menu import amend_spec_menu, create_spec_menu, delete_spec_menu, display_single_spec_menu, display_specs_menu, show_menu

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

            if display_choice == '1': # display all specs
                print("\nAll specifications:\n")
                display_all_specs(csv)

            elif display_choice == '2': # display single spec
                display_single_spec_choice = display_single_spec_menu()         
                if display_single_spec_choice == '1':
                    search_input = input("\nEnter SpecID: ")
                    display_single_spec(csv, display_single_spec_choice, search_input)
                elif display_single_spec_choice == '2':
                    search_input = input("\nEnter spec name: ").lower()
                    display_single_spec(csv, display_single_spec_choice, search_input)
                else:
                    break

            else:
                break

        elif choice == '2': # create new spec and append to csv file
            fields = create_spec_menu()
            create_new_spec(CSV_FILE_PATH, fields)
            csv = load_specs(CSV_FILE_PATH)

        elif choice == '3': # amend a specification
            amend_spec_choice = amend_spec_menu()

        elif choice == '4': # delete a specification
            delete_spec_choice = delete_spec_menu()

            if delete_spec_choice == '1':
                search_input = input("\nEnter SpecID: ")
                delete_spec(CSV_FILE_PATH, delete_spec_choice, search_input)
            elif delete_spec_choice == '2':
                search_input = input("\nEnter name: ").lower()
                delete_spec(CSV_FILE_PATH, delete_spec_choice, search_input)
            else:
                break

            csv = load_specs(CSV_FILE_PATH)

        elif choice == '5': # quit app
            quit_program()


def quit_program():
    print("\nExiting specification handler. Goodbye!")
    sys.exit(0)
    
# Standard 'entry point' check to prevent running when imported elsewhere, e.g. when unit testing
if __name__ == '__main__':
    main()