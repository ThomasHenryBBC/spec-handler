# Core application logic, imports functions to manage flow of program

import sys  # Allows use of sys.ext(), which is preferred over quit() to exit program
from csv_manager import load_specs, display_specs, CSV_FILE_PATH
from menu import display_menu

# Entry point of spec handler app
def main():
    
    # Load specification csv
    csv = load_specs(CSV_FILE_PATH)

    # Display specs
    print('\n Specifications loaded:\n')
    display_specs(csv)

    choice = display_menu()

    if choice == '1':
        pass
    elif choice == '2':
        pass
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