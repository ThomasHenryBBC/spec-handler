# Core application logic, imports functions to manage flow of program

import sys  # allows use of sys.ext(), which is preferred over quit() to exit program
from csv_manager import amend_spec, create_new_spec, delete_spec, load_specs, display_all_specs, display_single_spec, CSV_FILE_PATH
from menu import amend_spec_menu, amend_field_menu, create_spec_menu, delete_spec_menu, display_single_spec_menu, display_specs_menu, show_menu, get_confirmation

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
                display_single_spec_choice = display_single_spec_menu() # choice from menu to search by spec_id or by name   
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
            amend_choice, search_input = amend_spec_menu()

            if amend_choice == '3':
                continue

            print("\nSearching for specification...\n")
            record_found = display_single_spec(csv, amend_choice, search_input) # Returns true if search finds valid spec

            if record_found:
                field_choice, new_value = amend_field_menu()

                # Convert menu choice to csv column index
                field_index = int(field_choice) - 1

                success = amend_spec(CSV_FILE_PATH, amend_choice, search_input, field_index, new_value)
                if success:
                    print("\nSuccess! Specification updated successfully.")
                else:
                    print("Error. Failed to update Specification.")

                # Reload spec data to memory
                csv = load_specs(CSV_FILE_PATH)
            
            else:
                print(f"\nError. No specification found matching '{search_input}")



        elif choice == '4': # delete a specification
            delete_spec_choice = delete_spec_menu()

            if delete_spec_choice == '1':
                search_input = input("\nEnter SpecID: ")
            elif delete_spec_choice == '2':
                search_input = input("\nEnter name: ").lower()
            else:
                break

            # Prompt user for confirmation
            if get_confirmation(f"Delete the specification '{search_input}'"):
                success = delete_spec(CSV_FILE_PATH, delete_spec_choice, search_input)

                if success:
                    print("\nSuccess! Specification deleted.")
                else:
                    print(f"\nError. No specification found matching '{search_input}'")
            else:
                print("\nDeletion cancelled.")

            csv = load_specs(CSV_FILE_PATH)


        elif choice == '5': # quit app
            quit_program()

# TODO: Add confirmation prompt
def quit_program():
    print("\nExiting specification handler. Goodbye!")
    sys.exit(0)
    
# Standard 'entry point' check to prevent running when imported elsewhere, e.g. when unit testing
if __name__ == '__main__':
    main()