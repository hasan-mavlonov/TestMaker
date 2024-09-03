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


def user_page(username):
    text = """
    1. Create a test.
    2. See all tests.
    3. Edit a test.
    4. Delete a test.   
    5. Get my id
    """
    user_input = input(text)
    if user_input == '1':
        create_test(username)
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
