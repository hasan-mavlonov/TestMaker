from database_config.db_settings import execute_query
from queries.testsqueries import CREATE_TEST


class TestManager:
    def __init__(self, test_name):
        self.test_name = test_name

    def create_test(self, user_id, status):
        try:
            params = (user_id, self.test_name, status)
            result = execute_query(CREATE_TEST, params, fetch='one')
            print(result)
            return True
        except Exception as e:
            print(e)
            return False
