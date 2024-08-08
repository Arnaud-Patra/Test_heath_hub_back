import json
import pytest
from unittest.mock import mock_open, patch
from models.usermodel import UserModel
from services.userstorage import UserStorage  # Replace with the actual import path
MOCK_DATA = [
        {"id": 1, "name": "John", "email": "john@example.com"},
        {"id": 2, "name": "Jane", "email": "jane@example.com"}
    ]
@pytest.fixture
def user_storage():
    """Fixture to create a UserStorage instance."""
    return UserStorage()

def test_load_users_success(user_storage, mocker):
    """Test load_users method with valid JSON data."""
    mock_file = mock_open(read_data=json.dumps(MOCK_DATA))

    mock_open_file = mocker.patch("builtins.open", mock_file)
    
    result = user_storage.load_users()
    
    assert result == MOCK_DATA
    mock_open_file.assert_called_once_with('database.json', 'r')

def test_load_users_file_not_found(user_storage, mocker):
    """Test load_users method when the file is not found."""
    mock_file = mock_open(read_data=json.dumps(MOCK_DATA))
    mock_file.side_effect=FileNotFoundError
    mocker.patch("builtins.open", mock_file)
    
    result = user_storage.load_users()
    
    assert result is None

def test_load_users_json_decode_error(user_storage, mocker):
    """Test load_users method when there is a JSON decode error."""
    mocker.patch("builtins.open", mock_open(read_data="{invalid_json"))
    
    result = user_storage.load_users()
    
    assert result is None

def test_get_user_by_id_found(user_storage):
    """Test get_user_by_id method when the user is found."""
    users = [
        {"id": 1, "name": "John", "email": "john@example.com"},
        {"id": 2, "name": "Jane", "email": "jane@example.com"}
    ]
    
    result = user_storage.get_user_by_id(users, 1)
    
    assert result == {"id": 1, "name": "John", "email": "john@example.com"}

def test_get_user_by_id_not_found(user_storage):
    """Test get_user_by_id method when the user is not found."""
    users = [
        {"id": 1, "name": "John", "email": "john@example.com"},
        {"id": 2, "name": "Jane", "email": "jane@example.com"}
    ]
    
    result = user_storage.get_user_by_id(users, 999)  # A non-existent ID
    
    assert result is None

def test_find_last_id(user_storage):
    """Test _find_last_id method."""
    users = [
        {"id": 1, "name": "John", "email": "john@example.com"},
        {"id": 2, "name": "Jane", "email": "jane@example.com"}
    ]
    
    result = user_storage._find_last_id(users)
    
    assert result == 2

def test_create_user_success(user_storage, mocker):
    """Test create_user method with valid data."""
    new_user = UserModel(name="Alice", username="alice123", email="alice@example.com", address={}, phone="123-456-7890", website="alice.com", company={})
    mock_existing_data = [
        {"id": 1, "name": "John", "email": "john@example.com"},
        {"id": 2, "name": "Jane", "email": "jane@example.com"}
    ]
    mock_open_file = mocker.patch("builtins.open", mock_open(read_data=json.dumps(mock_existing_data)))
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

    result = user_storage.create_user(new_user)

    assert result == "User added to database."
    mock_open_file.assert_called_once_with('database.json', 'r')
    mock_dump.assert_called_once()

def test_create_user_file_not_found(user_storage, mocker):
    """Test create_user method when the file is not found."""
    new_user = UserModel(name="Alice", username="alice123", email="alice@example.com", address={}, phone="123-456-7890", website="alice.com", company={})
    mocker.patch("builtins.open", mock_open(side_effect=FileNotFoundError))

    result = user_storage.create_user(new_user)

    assert result == "status"

def test_create_user_json_decode_error(user_storage, mocker):
    """Test create_user method when there is a JSON decode error."""
    new_user = UserModel(name="Alice", username="alice123", email="alice@example.com", address={}, phone="123-456-7890", website="alice.com", company={})
    mocker.patch("builtins.open", mock_open(read_data="{invalid_json"))

    result = user_storage.create_user(new_user)

    assert result == "status"