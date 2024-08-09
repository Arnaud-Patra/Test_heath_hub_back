from typing import List
from models.usermodel import UserModel
from services.abstractservice import AbstractService
from services.userstorage import UserStorage


class UserService(AbstractService):
    def __init__(self) -> None:
        self.storage = UserStorage()
        super().__init__()

    def _get_all_users(self) -> List[dict]:
        """
        fetch all users from the storage
        Returns:
        List: list of all the users.
        """
        return self.storage.load_users()

        # would be interesting to do a parser here

    def get_user(self, user_id: int) -> dict:
        """
        Get a specific user from the list of users

        Parameters:
        user_id (int): The user id to retrieve given by the API

        Returns:
        dict: The dictionary of the user wanted.
        """
        users = self._get_all_users()

        return self.storage.get_user_by_id(users, user_id)

    def create_user(self, user_data: UserModel) -> str:
        """
        Add new user in the database

        Parameters:
        user_data (UserModel): The user data to load into the database

        Returns:
        str: Status of the load
        """

        return self.storage.create_user(user_data)
