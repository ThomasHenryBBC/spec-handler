# Automated unit tests to prove code functionality and add quality assurance
# To run automated tests ensure pytest is installed with "pip install pytest" and then run "pytest unittests.py" in the terminal

from app import main
from menu import amend_spec_menu, amend_field_menu, create_spec_menu, delete_spec_menu, display_single_spec_menu, display_specs_menu, show_menu, get_confirmation
from csv_manager import amend_spec, create_new_spec, delete_spec, load_specs, display_all_specs, display_single_spec
from validator import validate_field

def test_spec_id_validation():
    # Valid 6-digit ID
    is_valid, msg = validate_field(0, "036453")
    assert is_valid
    
    # Too short
    is_valid, msg = validate_field(0, "12345") 
    assert not is_valid
    assert msg == "SpecID must be exactly 6 digits (e.g., 036453)."
    
    # Contains letters
    is_valid, msg = validate_field(0, "123abc")
    assert not is_valid

def test_empty_string_validation():
    # Field 1 (name) cannot be empty
    is_valid, msg = validate_field(1, "Live Event Carousel")
    assert is_valid
    
    # Blank spaces should be stripped and flagged as empty
    is_valid, msg = validate_field(1, "   ") 
    assert not is_valid
    assert msg == "This field cannot be empty."

def test_version_validation():
    # Correct semantic versioning
    is_valid, msg = validate_field(2, "1.0.0")
    assert is_valid
    
    # Missing a number
    is_valid, msg = validate_field(2, "1.0")
    assert not is_valid
    
    # Contains a letter
    is_valid, msg = validate_field(2, "v1.0.0")
    assert not is_valid

def test_date_validation():
    # Valid date format
    is_valid, msg = validate_field(3, "22/10/2025")
    assert is_valid
    
    # Invalid date (February doesn't have 30 days)
    is_valid, msg = validate_field(3, "30/02/2025")
    assert not is_valid

def test_screenshot_validation():
    # Ends in .png
    is_valid, msg = validate_field(5, "image.png")
    assert is_valid
    
    # Ends in .jpg
    is_valid, msg = validate_field(5, "image.jpg")
    assert not is_valid

def test_boolean_validation():
    # Exact matches
    is_valid, msg = validate_field(7, "TRUE")
    assert is_valid
    is_valid, msg = validate_field(7, "FALSE")
    assert is_valid
    
    # Invalid boolean strings
    is_valid, msg = validate_field(7, "YES")
    assert not is_valid