# Automated unit tests to prove code functionality and add quality assurance
# To run automated tests ensure pytest is installed with "pip install pytest" and then run "pytest unittests.py" in the terminal

import pytest

from app import main, quit_program
from menu import amend_spec_menu, amend_field_menu, create_spec_menu, delete_spec_menu, display_single_spec_menu, display_specs_menu, show_menu, get_confirmation
from csv_manager import amend_spec, create_new_spec, delete_spec, load_specs, display_all_specs, display_single_spec
from validator import validate_field

# Fixture to avoid repetition of dummy spec csv data
@pytest.fixture
def dummy_csv(tmp_path):
    """Creates a temporary CSV file with 2 dummy records for testing."""
    filepath = tmp_path / "test_specifications.csv"

    # Standard header + 2 valid rows
    content = (
        "specId,name,version,dateFinalised,description,screenshotURL,labelsAndValues,implementationStatusWeb,implementationStatusTV,implementationStatusIOS,implementationStatusAndroid\n"
        "111111,Test Spec One,1.0.0,01/01/2025,First test,img1.png,label1,TRUE,FALSE,TRUE,FALSE\n"
        "222222,Test Spec Two,2.0.0,02/02/2025,Second test,img2.png,label2,FALSE,TRUE,FALSE,TRUE\n"
    )
    filepath.write_text(content, encoding="utf-8")

    return str(filepath) # Returns the file path as a string for the manager to use


# Test csv_manager functions

def test_load_specs(tmp_path):
    # Create temp file path
    temp_file = tmp_path / "test_data.csv"
    
    # Write dummy CSV data
    temp_file.write_text("specId,name\n123456,Hero Section\n", encoding="utf-8")
    
    # Test function using the temporary file
    data = load_specs(temp_file)
    
    assert len(data) == 2 # Should have 1 header row + 1 data row
    assert data[1][1] == "Hero Section" # The name should match

# Test menu functions

def test_get_confirmation_yes(monkeypatch):
    # Use monkeypatch to hijack the input() function to automatically return 'y'
    monkeypatch.setattr('builtins.input', lambda _: 'y')
    
    # Run the function to return True
    result = get_confirmation("delete this test")
    assert result is True

def test_get_confirmation_no(monkeypatch):
    # Hijack the input() function to automatically return 'n'
    monkeypatch.setattr('builtins.input', lambda _: 'n')
    
    result = get_confirmation("delete this test")
    assert result is False

# Test app

def test_quit_program_exits(monkeypatch):
    # Mock get_confirmation to return True (simulating quit)
    monkeypatch.setattr('app.get_confirmation', lambda _: True)
    
    with pytest.raises(SystemExit):
        quit_program()

# Test validator functions

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