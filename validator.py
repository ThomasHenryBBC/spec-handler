# Validates CRUD actions before implementation in csv_manager

import datetime # Assists with validating date fields

def validate_field(field_index, value):
    # Validates a string value based on field index in the CSV (0 to 10), and returns a tuple containg validity and an error message

    value = value.strip()

    # Field 0: specID (Must be exactly 6 digits)
    if field_index == 0:
        if len(value) != 6 or not value.isdigit():
            return False, "SpecID must be exactly 6 digits (e.g., 036453)."

    # Fields 1, 4, 6: name, description, labelsAndValues (Must not be empty)
    elif field_index in [1, 4, 6]:
        if not value:
            return False, "This field cannot be empty."

    # Field 2: version (Must be Semantic Versioning e.g., 1.0.0)
    elif field_index == 2:
        parts = value.split('.')
        if len(parts) != 3 or not all(p.isdigit() for p in parts):
            return False, "Version must be in semantic format X.Y.Z (e.g., 1.0.0)."

    # Field 3: dateFinalised (Must be DD/MM/YYYY)
    elif field_index == 3:
        try:
            # datetime.strptime tries to parse the string using the format code
            datetime.datetime.strptime(value, "%d/%m/%Y")
        except ValueError:
            return False, "Date must be in DD/MM/YYYY format (e.g., 22/10/2024)."

    # Field 5: screenshotURL (Must end with .png)
    elif field_index == 5:
        if not value.lower().endswith('.png') or not value:
            return False, "Screenshot URL must end with '.png'."

    # Fields 7-10: implementation statuses (Must be TRUE or FALSE)
    elif field_index in [7, 8, 9, 10]:
        if value.upper() not in ['TRUE', 'FALSE']:
            return False, "Status must be exactly 'TRUE' or 'FALSE'."

    # If it doesn't fail any of the above checks, it is valid. No error needs to be returned
    return True, ""