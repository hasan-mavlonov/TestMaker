from managers.usersmanager import UsersManager


def register_page() -> None:
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    if not UsersManager(username).check_existence():
        if UsersManager(username).create_user(password):
            print('User created successfully')


def auth_menu() -> None:
    text = """
    1. Login
    2. Register
    3. Logout
    """
    user_input = input(text)
    if user_input == "1":
        pass
    elif user_input == "2":
        register_page()
    elif user_input == "3":
        pass


if __name__ == '__main__':
    auth_menu()
