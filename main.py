from managers.usersmanager import UsersManager


def user_page(username):
    a = input('Hello user')


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
