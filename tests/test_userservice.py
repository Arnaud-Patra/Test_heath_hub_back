import pytest
from unittest.mock import MagicMock

from services.userservice import UserService

    
@pytest.fixture
def mock_user_storage(mocker):
    """Mock UserStorage"""
    mock_storage_patch = mocker.patch('services.userservice.UserStorage')
    return mock_storage_patch

@pytest.fixture
def user_services(mock_user_storage):
    """Fixture to create UserServices instance with mocked UserStorage"""
    return UserService()

def test_get_all_users(user_services, mock_user_storage):
    # Arrange
    mock_user_storage().load_users.return_value = [
        {"id": 1, "name": "John"},
        {"id": 2, "name": "Jane"}
    ]

    # Act
    result = user_services._get_all_users()

    # Assert
    assert result == [
        {"id": 1, "name": "John"},
        {"id": 2, "name": "Jane"}
    ]

def test_get_user(user_services, mock_user_storage):
    # Arrange
    mock_user_storage().load_users.return_value = [
        {"id": 1, "name": "John"},
        {"id": 2, "name": "Jane"}
    ]
    mock_user_storage().get_item_by_id.return_value = {"id": 1, "name": "John"}

    # Act
    result = user_services.get_user(1)

    # Assert
    assert result == {"id": 1, "name": "John"}

    """Test  user is not found"""
    # Arrange
    mock_user_storage().load_users.return_value = [
        {"id": 1, "name": "John"},
        {"id": 2, "name": "Jane"}
    ]
    mock_user_storage().get_item_by_id.return_value = None

    # Assuming 999 is an invalid user_id
    result = user_services.get_user(999)

    assert result is None

