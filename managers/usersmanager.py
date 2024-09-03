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
            result = execute_query(queries.usersqueries.CREATE_USER, params, fetch='one')
            print(result)
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

    def check_password(self, password):
        try:
            password = hashlib.sha256(password.encode()).hexdigest()
            params = (self.full_name,)
            result = execute_query(queries.usersqueries.GET_PASSWORD, params, fetch="one")
            for passwords in result:
                if passwords == password:
                    return True
        except Exception as e:
            print(e)
            return False

    def get_user_id(self):
        try:
            params = (self.full_name,)
            result = execute_query(queries.usersqueries.GET_USER_ID, params, fetch="one")
            for user_id in result:
                return user_id
        except Exception as e:
            print(e)
