from database_config.db_settings import execute_query
from queries.testsqueries import CREATE_TEST, READ_ALL_TESTS, READ_USER_TEST, UPDATE_TEST, DELETE_TEST


class TestManager:
    def __init__(self, test_name):
        self.test_name = test_name

    def create_test(self, user_id, status):
        try:
            params = (user_id, self.test_name, status)
            result = execute_query(CREATE_TEST, params, fetch='one')
            return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def read_all_tests():
        try:
            result = execute_query(READ_ALL_TESTS, fetch='all')
            for test in result:
                for tests in test:
                    print(tests)
            return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def read_user_test(user_id):
        try:
            params = (user_id,)
            result = execute_query(READ_USER_TEST, params, fetch='one')
            for test in result:
                print(test)
            return True
        except Exception as e:
            print(e)
            return False

    def check_existence(self):
        try:
            params = (self.test_name,)
            result = execute_query(READ_ALL_TESTS, params, fetch='one')
            for test in result:
                if test == self.test_name:
                    return True
            return False
        except Exception as e:
            print(e)
            return False

    def change_test_name(self, new_name):
        try:
            params = (new_name, self.test_name,)
            result = execute_query(UPDATE_TEST, params, fetch='one')
            return True
        except Exception as e:
            print(e)
            return False

    def delete_test(self):
        try:
            params = (self.test_name, )
            result = execute_query(DELETE_TEST, params)
            return True
        except Exception as e:
            print(e)
            return False
