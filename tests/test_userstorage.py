import json
import pytest
from unittest.mock import call, mock_open, patch
from models.usermodel import UserModel
from services.userstorage import UserStorage

MOCK_DATA = [
        {"id": 1, "name": "John", "email": "john@example.com"},
        {"id": 2, "name": "Jane", "email": "jane@example.com"}
    ]

@pytest.fixture
def user_storage():
    return UserStorage()

def test_load_users_success(user_storage):
    """Test load is successful """
    mocked_open = mock_open(read_data=json.dumps(MOCK_DATA))

    # Use patch to replace the built-in open function with the mock_open
    with patch('builtins.open', mocked_open):
        result = user_storage.load_users()
    
    mocked_open.assert_called_once_with('database.json', 'r')

    assert result == MOCK_DATA

def test_load_users_file_not_found(user_storage):
    """Test load_users method when the file is not found."""
    mocked_open = mock_open(read_data=json.dumps(MOCK_DATA))
    mocked_open.side_effect = FileNotFoundError

    with patch('builtins.open', mocked_open):
        result = user_storage.load_users()
    
    assert result is None

def test_load_users_json_decode_error(user_storage):
    """Test load_users method when there is a JSON decode error."""
    mocked_open = mock_open(read_data="{invalid json")

    with patch('builtins.open', mocked_open):

        result = user_storage.load_users()
    assert result is None

def test_get_user_by_id_found(user_storage):
    """Test get_user_by_id method when the user is found."""  
    result = user_storage.get_user_by_id(MOCK_DATA, 1)
    
    assert result == {"id": 1, "name": "John", "email": "john@example.com"}

def test_get_user_by_id_not_found(user_storage):
    """Test get_user_by_id method when the user is not found."""
  
    result = user_storage.get_user_by_id(MOCK_DATA, 999)  # A non-existent ID
    
    assert result is None

def test_find_last_id(user_storage):
    """Test _find_last_id method."""
    result = user_storage._find_last_id(MOCK_DATA)
    
    assert result == 2

def test_create_user_success(user_storage, mocker):
    """Test create_user method with valid data."""
    new_user = UserModel(name="Alice", username="alice123", email="alice@example.com", address={}, phone="123-456-7890", website="alice.com", company={})

    mocked_open = mock_open(read_data=json.dumps(MOCK_DATA))
    mock_dump = mocker.patch("json.dump")

    # Mock the model_dump_json method
    mocker.patch.object(UserModel, 'model_dump_json', return_value=json.dumps({
        "name": "Alice",
        "username": "alice123",
        "email": "alice@example.com",
        "address": {},
        "phone": "123-456-7890",
        "website": "alice.com",
        "company": {}
    }))

    # Use patch to replace the built-in open function with the mock_open
    with patch('builtins.open', mocked_open):
        result = user_storage.create_user(new_user)

    assert result == "User added to database."
    mocked_open.assert_has_calls([call('database.json', 'r')])
    mock_dump.assert_called_once()

def test_create_user_file_not_found(user_storage, mocker):
    """Test create_user method when the file is not found."""
    new_user = UserModel(name="Alice", username="alice123", email="alice@example.com", address={}, phone="123-456-7890", website="alice.com", company={})
    mocked_open = mock_open(read_data=json.dumps(MOCK_DATA))
    mocked_open.side_effect = FileNotFoundError

    with patch('builtins.open', mocked_open):
        result = user_storage.create_user(new_user)

    assert result == "The file was not found."

def test_create_user_json_decode_error(user_storage, mocker):
    """Test create_user method when there is a JSON decode error."""
    new_user = UserModel(name="Alice", username="alice123", email="alice@example.com", address={}, phone="123-456-7890", website="alice.com", company={})
    
    mocked_open = mock_open(read_data="{invalid_json")

    with patch('builtins.open', mocked_open):
        result = user_storage.create_user(new_user)

    assert result == "Error decoding JSON."