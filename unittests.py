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

def test_load_specs(dummy_csv):
    # Test function using the dummy fixture
    data = load_specs(dummy_csv)
    
    assert len(data) == 3 # Should have 1 header row + 2 data row
    assert data[1][0] == "111111" # The ID should match first column of first spec in dummy fixture

def test_display_all_specs(dummy_csv, capsys):
    # capsys captures print() output
    data = load_specs(dummy_csv)
    display_all_specs(data)
    
    captured = capsys.readouterr()
    assert "Test Spec One" in captured.out
    assert "Test Spec Two" in captured.out

def test_display_single_spec_found(dummy_csv, capsys):
    data = load_specs(dummy_csv)
    # Search by SpecID (1) for "111111"
    found = display_single_spec(data, '1', "111111")
    
    captured = capsys.readouterr()
    assert found is True
    assert "Test Spec One" in captured.out
    assert "Test Spec Two" not in captured.out # Should only print the one searched for

def test_display_single_spec_not_found(dummy_csv):
    data = load_specs(dummy_csv)
    # Search by Name (2) for a non-existent name
    found = display_single_spec(data, '2', "not a spec")
    assert found is False

def test_create_new_spec(dummy_csv):
    new_row = ["333333", "Test Spec Three", "3.0.0", "03/03/2025", "Third test", "img3.png", "label3", "TRUE", "TRUE", "TRUE", "TRUE"]
    create_new_spec(dummy_csv, new_row)
    
    # Reload to verify it was saved
    data = load_specs(dummy_csv)
    assert len(data) == 4 # Header + 3 rows
    assert data[-1][1] == "Test Spec Three"

def test_amend_spec(dummy_csv):
    # Search by ID ('1') for '111111', change field index 1 (name) to 'Amended Name'
    success = amend_spec(dummy_csv, '1', '111111', 1, "Amended Name")
    assert success is True
    
    data = load_specs(dummy_csv)
    assert data[1][1] == "Amended Name"

def test_delete_spec(dummy_csv):
    # Search by ID ('1') for '222222' and delete
    success = delete_spec(dummy_csv, '1', '222222')
    assert success is True
    
    data = load_specs(dummy_csv)
    assert len(data) == 2 # Header + remaining row (111111)


# Test Menu UI functions

def test_show_menu(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '1')
    assert show_menu() == '1'

def test_display_specs_menu(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '2')
    assert display_specs_menu() == '2'

def test_display_single_spec_menu(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '3')
    assert display_single_spec_menu() == '3'

def test_delete_spec_menu(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '1')
    assert delete_spec_menu() == '1'

def test_get_confirmation(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'y')
    assert get_confirmation("test") is True

def test_amend_spec_menu(monkeypatch):
    # The user types '1' (Search by ID), then '111111'
    inputs = iter(['1', '111111'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    choice, search_val = amend_spec_menu()
    assert choice == '1'
    assert search_val == '111111'

def test_amend_field_menu(monkeypatch):
    # The user types '2' (Name field), then types 'New Valid Name'
    inputs = iter(['2', 'New Valid Name'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    field_choice, new_val = amend_field_menu()
    assert field_choice == '2'
    assert new_val == 'New Valid Name'

def test_create_spec_menu(monkeypatch):
    # The test user types all 11 fields correctly
    inputs = iter([
        '999999', 'New Spec', '1.0.0', '10/10/2025', 'Desc', 
        'img.png', 'lbl', 'TRUE', 'FALSE', 'TRUE', 'FALSE'
    ])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    fields = create_spec_menu()
    assert len(fields) == 11
    assert fields[0] == '999999'
    assert fields[7] == 'TRUE'


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