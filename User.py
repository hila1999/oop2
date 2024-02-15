from Post import PostFactory


class User:

    def __init__(self, name: str, passord: str ,is_connected: bool=None ):
        self.name = name
        self.passord = passord
        self.is_connected = is_connected
        self.followers = [] # how is follow after hime
        self.my_notifications = []
        self.observers = []
        self.my_posts = []

    def __repr__(self):
        return f"User name: {self.name}, Number of posts: {self.my_posts.__len__()}, Number of followers:{self.followers.__len__()} "

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, notifications):
        for observer in self.observers:
            observer.update(self, notifications)

    def update(self, observable, notifications):
        self.my_notifications.append(notifications)

    def like(self,post):
        if self not in post.liked_by:
         post.liked_by.append(self)
        else:
            pass
    def comment(self,post):
        if self not in post.comments:
            post.comments.append(self)

    def print_notifications(self):
        print(f"{self.name}'s notifications:")
        for notifications in self.my_notifications:
            print(f"{notifications}")
    def follow(self, u2):
        if not self.is_connected:
            print("Not connected")
        if self in u2.followers:
            pass
        else:
            u2.followers.append(self)
            u2.observers.append(self)
            print(f"{self.name} started following {u2.name}")
    def unfollow(self, u2):
        if not self.is_connected:
            print("Not connected")
        if self in u2.followers:
            u2.followers.remove(self)
            u2.observers.remove(self)
            print(f"{u2.name} unfollowed {self.name}")


    def publish_post(self, type: str, dataWord: str, price = None, location:str = None, available = True):
        return PostFactory.process_type(self, type, dataWord, price, location, available = True)




