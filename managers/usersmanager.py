import queries.usersqueries
from queries.usersqueries import *
from database_config.db_settings import execute_query
import hashlib


class UsersManager:
    def __init__(self, full_name):
        self.full_name = full_name

    def create_user(self, password):
        try:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            params = (self.full_name, hashed_password)
            result = execute_query(queries.usersqueries.CREATE_USER, params)
            if result is None:
                return True
        except Exception as e:
            print(e)
            return False

    def check_existence(self):
        try:
            params = (self.full_name,)
            result = execute_query(queries.usersqueries.READ_USER_BY_NAME, params, fetch="one")
            if result is None:
                return False
            else:
                return True
        except Exception as e:
            print(e)
            return False

    def delete_user(self):
        try:
            params = (self.full_name,)
            result = execute_query(queries.usersqueries.DELETE_USER, params)
            if result is None:
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False
