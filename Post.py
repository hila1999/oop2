import User
from enum import Enum
import matplotlib.pyplot as plt



# this method define all the types of the post
class PostTypes(Enum):
    TextPost = "Text"
    ImagePost = "Image"
    SalePost = "Sale"
class PostFactory:
    @staticmethod
    def process_type(self, type, dataWord, price, location, available):
        if type == "Text":
            post_temp = (TextPost(self, dataWord))
        elif type == "Image":
            post_temp = (ImagePost(self, dataWord))
        elif type == "Sale":
            post_temp = (SalePost(self, dataWord, price, location, available))
        else:
            print(f"Error: Invalid post type '{type}'.")
            return
        post_temp.add_observer(self)
        print(str(post_temp))
        return post_temp
    def __init__(self, name:User, dataWorld:str) :
        self.name = name
        self.dataWorld = dataWorld
        self.liked_by = []
        self.observers = []
        self.comments = []
        name.notify_observers(f"{name.name} has a new post")

    def add_observer(self, observer):
        self.observers.append(observer)


    def notify_observers(self, notifications):
        for observer in self.observers:
            observer.update(self, notifications)


    def like(self, u2 :User):
        if not u2.is_connected:
            print("Not connected")
        if u2 not in self.liked_by:
            self.liked_by.append(u2)
            if u2.name != self.name.name:
                self.notify_observers(f"{u2.name} liked your post")
                print(f"notification to {self.name.name}: {u2.name} liked your post")
    def comment(self, u2, comment:str=""):
        if not u2.is_connected:
            print("Not connected")
        if u2.name != self.name.name:
            self.notify_observers(f"{u2.name} commented on your post")
            print(f"notification to {self.name.name}: {u2.name} commented on your post: {comment}")




class TextPost(PostFactory):
    def __init__(self, name: User,  dataWorld: str):
        super().__init__(name, dataWorld)

    def __str__(self):
        return  f'{self.name.name} published a post:\n"{self.dataWorld}"\n'



class ImagePost(PostFactory):
    def __init__(self, name:User, img:str):
        super().__init__(name, img)
    def display(self):
        image_rgb = plt.imread(self.dataWorld)
        plt.imshow(image_rgb)
        plt.axis('off')
        plt.show()
        print("Shows picture")
    def __str__(self):
        return f"{self.name.name} posted a picture\n"

class SalePost(PostFactory):
    def __init__(self, name:User, dataWorld:str, price:int ,location:str=None, available:bool = True):
        super().__init__(name,dataWorld)
        # self.dataWorld = dataWorld
        self.price = price
        self.location = location
        self.available = available



    # def  print(self,dataWord:str,price, location):
    #     print(f"{self.name} posted a product for sale:")
    #     print(f"For sale! {dataWord}, price: {price}, pickup from: {location}")
    def discount(self,  discount_percentage:int, passord:str):
        if  self.name.passord == passord:
            output: float = self.price - (self.price * discount_percentage / 100)
            self.price = output
            print(f"Discount on {self.name.name} product! the new price is: {self.price}")
        else:
            pass
    def sold(self, passord:str):
        if self.name.passord == passord:
            self.available = False
            print(f"{self.name.name}'s product is sold")

    def __str__(self):
         if self.available:
             prefix = "For sale! "
         else:
             prefix = "Sold! "
         return f"{self.name.name} posted a product for sale:\n{prefix}{self.dataWorld}, price: {self.price}, pickup from: {self.location}\n"
