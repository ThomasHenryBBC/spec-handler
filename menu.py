# Handles the user interface

def display_menu():
    while True:
        print("\nSpecification Manager\n")
        print("1. Display specifications")
        print("2. Add a new specification")
        print("3. Amend a specification")
        print("4. Delete a specification")
        print("5. Quit\n")

        choice = input("What would you like to do?: ").strip()

        if choice in ['1', '2', '3', '4', '5']:
            return choice
        else:
            print("\nInvalid choice. Please enter a number 1 to 5.")