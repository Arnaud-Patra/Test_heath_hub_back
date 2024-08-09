import pytest
from unittest.mock import MagicMock, patch

from services.userservice import UserService


@pytest.fixture
def mock_user_storage(mocker):
    """Mock UserStorage"""
    return mocker.patch('services.userservice.UserStorage')

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
    # Create the patch object
    mock_users = [
        {"id": 1, "name": "John"},
        {"id": 2, "name": "Jane"}
    ]
    patcher = patch.object(UserService, '_get_all_users', return_value=mock_users)
    mock_get_all_users = patcher.start()

    mock_user_storage().get_user_by_id.return_value = {"id": 1, "name": "John"}

    # Act
    result = user_services.get_user(1)

    # Assert
    assert result == {"id": 1, "name": "John"}

    """Test  user is not found"""
    mock_user_storage().get_user_by_id.return_value = None

    # Assuming 999 is an invalid user_id
    result = user_services.get_user(999)

    assert result is None

def test_create_user(user_services, mock_user_storage):
    """ Test create user storage call"""
    mock_user_storage().create_user.return_value = "User added to database"
    mock_model = MagicMock()

    result = user_services.create_user(mock_model)

    mock_user_storage().create_user.assert_called_once_with(mock_model)
    assert result is "User added to database"
