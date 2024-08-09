# would be a good idea to 
import json
from typing import List

from models.usermodel import UserModel

class UserStorage:

    def __init__(self) -> None:
            pass

    def load_users(self) -> List[dict]:
        """
        mock load from SQL or other source
        
        Returns:
            dict: List of all the users existing
        """

        try:
            with open('database.json', 'r') as file:
                data = json.load(file)

            return data
        
        except FileNotFoundError:
            print("The file was not found.")
        except json.JSONDecodeError:
            print("Error decoding JSON.")

        return None

    def get_user_by_id(self, users: dict, search_id: int) -> dict:
        """
        Retrieve a dictionary from a list of dictionaries by the 'id' field.
        
        Parameters:
            users (list): List of dictionaries.
            search_id (int): The id to search for.
            
        Returns:
            user (dict): The dictionary with the matching id, or None if not found.
        """
        for user in users:
            if user['id'] == search_id:
                return user
        return None
    
    def _find_last_id(self, users) -> int:
        """
        Search the database for the last id stored
        
        Parameters: 
            users (list): the data from the database
        
        Returns:
            last_id(int): The last id from the database
        """
        ids = []
        for user in users:
            ids.append(user["id"])
        return max(ids)


    def create_user(self, user_data: UserModel) -> str:
        """
        Add new user in the database
        
        Parameters:
            user_data (dict): The user data to load into the database
            User should be a dictionnary without the 'id' field
        Returns:
            str: Status of the load
        """
        try:
            with open('database.json', 'r') as file:
                users = json.load(file)
            user_data.id = self._find_last_id(users) + 1 # increment id by one

            user_data_json = json.loads(user_data.model_dump_json())
            users.append(user_data_json)
        
            with open("database.json", "w") as jsonFile:
                json.dump(users, jsonFile)
                return "User added to database."

        except FileNotFoundError:
            return "The file was not found."
        except json.JSONDecodeError:
            return "Error decoding JSON."
