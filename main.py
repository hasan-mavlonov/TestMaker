from managers.usersmanager import UsersManager
from managers.testsmanager import TestManager


def create_test(username):
    user_id = UsersManager(username).get_user_id()
    name = input('Enter the name of the test: ')
    status = input('Enter the status of the test(active/inactive: '.lower())
    print(status)
    if status == 'active' or status == 'inactive':
        print('Hello')
        if TestManager(name).create_test(user_id, status):
            print('Test created successfully')


def get_user_tests(username):
    user_id = UsersManager(username).get_user_id()
    if TestManager.read_user_test(user_id):
        test_page(username)


def test_page(username):
    text = """
    1. Create a test.
    2. See all tests.
    3. See my tests
    4. Edit a test.
    5. Delete a test.  
    """
    user_input = input(text)
    if user_input == '1':
        create_test(username)
    elif user_input == '2':
        TestManager.read_all_tests()
    elif user_input == '3':
        get_user_tests(username)
    elif user_input == '4':
        test_name = input('Enter the name of the test: ')
        user_id = UsersManager(username).get_user_id()
        if TestManager(test_name).check_if_owner(user_id):
            new_name = input('Enter the new name of the test: ')
            if TestManager(test_name).change_test_name(new_name):
                print('Test updated successfully')
                test_page(username)
    elif user_input == '5':
        test_name = input('Enter the name of the test: ')
        if TestManager(test_name).check_existence():
            if TestManager(test_name).delete_test():
                print('Test deleted successfully')
                test_page(username)


def question_page(username):
    test_name = input('Enter the name of the test: ')
    user_id = UsersManager(username).get_user_id()
    if TestManager(test_name).check_if_owner(user_id):
        text = """
        1. Create a question
        2. See all question from the test
        3. Edit a question
        4. Delete a question
        """
        user_input = input(text)
    else:
        print("The test wasn't found or you don\'t have an access for it!")
        user_page(username)


def user_page(username):
    text = """
    1. Tests | CRUD
    2. Questions | CRUD
    3. 
    5. Get my id
    """
    user_input = input(text)
    if user_input == '1':
        test_page(username)
    elif user_input == '2':
        pass
    elif user_input == '5':
        print(UsersManager(username).get_user_id())


def login_page() -> None:
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    if UsersManager(username).check_existence():
        if UsersManager(username).check_password(password):
            print('Login successful')
            user_page(username)
        else:
            print('Incorrect login or password. Try again!')
            auth_menu()


def register_page() -> None:
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    if not UsersManager(username).check_existence():
        if UsersManager(username).create_user(password):
            print('User created successfully')
            auth_menu()


def auth_menu() -> None:
    text = """
    1. Login
    2. Register
    3. Logout
    """
    user_input = input(text)
    if user_input == "1":
        login_page()
    elif user_input == "2":
        register_page()
    elif user_input == "3":
        pass


if __name__ == '__main__':
    auth_menu()
