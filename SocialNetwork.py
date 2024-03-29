from typing import Set

from User import User


class SocialNetwork:
    _instance = None

    def __new__(cls, *args, **kwargs):  # A template singclton that makes sure we only created one network
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, name):
        if self._initialized:
            return
        self.name = name
        self.network = {}
        self.logged_in_users: Set[User] = set()
        print(f"The social network {self.name} was created!")
        self._initialized = True

    def __str__(self):
        users_info = [str(self.network[username]) for username in self.network]  # List comprehension to get user info
        return f"{self.name} social network:\n" + "\n".join(users_info) + "\n"

    def sign_up(self, username, password):
        if username in self.network:  # Checks that the selected username is not registered by another user
            print("Username already exists. Please choose another one.")
            return None
        if not 4 < len(password) < 8:  # Checks that the password is the correct length
            print("Password length should be between 4 and 8 characters.")
            return None
        user = User(username, password)
        self.network[username] = user
        self.logged_in_users.add(user)
        user.is_connected = True
        return user

    # def sign_up(self, username: str, password: str) -> User | None:
    #     if username in self.network:  # Checks that the selected username is not registered by another user
    #         print("Username already exists. Please choose another one.")
    #         return None
    #     if not 4 < len(password) < 8:  # Checks that the password is the correct length
    #         print("Password length should be between 4 and 8 characters.")
    #         return None
    #     user = User(username, password)
    #     return user

    def log_in(self, username, password):
        if username in self.network:
            user = self.network[username]
            if password == user.passord:
                if self.network[username] not in self.logged_in_users:
                    self.logged_in_users.add(self.network[username])
                    self.network[username].is_connected = True
                    print(f"{username} connected")
        else:
            print("Username does not exist. Please choose another one.")
            return

    def log_out(self, username):
        if username not in self.network:
            print("Username does not exist. Please choose another one.")
            return
        if self.network[username] not in self.logged_in_users:
            print("Username does not connected. Please choose another one.")
            return
        self.logged_in_users.remove(self.network[username])
        self.network[username].is_connected = False
        print(f"{username} disconnected")
