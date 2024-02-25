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

    def __str__(self):
        return f"User name: {self.name}, Number of posts: {self.my_posts.__len__()}, Number of followers: {self.followers.__len__()}"



    def notify_observers(self, notifications):
        for observer in self.observers:
            observer.update(self, notifications)

    def update(self, observable, notifications):
        self.my_notifications.append(notifications)

    # def like(self,post):
    #     if not self.is_connected:
    #         print("Not connected")
    #         return
    #     if self not in post.liked_by:
    #      post.liked_by.append(self)
    #     else:
    #         pass
    # def comment(self,post):
    #     if not self.is_connected:
    #         print("Not connected")
    #         return
    #     if self not in post.comments:
    #         post.comments.append(self)

    def print_notifications(self):
        print(f"{self.name}'s notifications:")
        for notifications in self.my_notifications:
            print(f"{notifications}")
    def follow(self, u2):
        if not self.is_connected:
            print("Not connected")
            return
        if self in u2.followers:
            pass
        if self.name != u2.name:
            u2.followers.append(self)
            u2.observers.append(self)
            print(f"{self.name} started following {u2.name}")
    def unfollow(self, u2):
        if not self.is_connected:
            print("Not connected")
        if self in u2.followers:
            u2.followers.remove(self)
            u2.observers.remove(self)
            print(f"{self.name} unfollowed {u2.name}")
            return None
        print("the user is not foolowes so we cant unfolow")


    def publish_post(self, type: str, dataWord: str, price = None, location:str = None, available = True):
        if not self.is_connected:
            print("Not connected")
            return
        post_now =PostFactory.process_type(self, type, dataWord, price, location, available = True)
        self.my_posts.append(post_now)
        return post_now


