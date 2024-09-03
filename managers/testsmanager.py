from database_config.db_settings import execute_query
from queries.testsqueries import CREATE_TEST, READ_TEST


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
            result = execute_query(READ_TEST, fetch='all')
            for test in result:
                for tests in test:
                    print(tests)
            return True
        except Exception as e:
            print(e)
            return False

    def check_existence(self):
        try:
            params = (self.test_name,)
            result = execute_query(READ_TEST, params, fetch='one')
            for test in result:
                for tests in test:
                    if tests == self.test_name:
                        return True
            return False
        except Exception as e:
            print(e)
            return False
