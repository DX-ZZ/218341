# 9-1餐馆
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Restaurant Name:" + self.restaurant_name.title())
        print("Cuisine Type:" + self.cuisine_type.title())

    def open_restaurant(self):
        print("welcome to our restaurant!")


restaurant = Restaurant("金拱门", "American")

print("our restaurant name is " + restaurant.restaurant_name + ".")
print("order " + restaurant.cuisine_type.title() + " food.")

restaurant.describe_restaurant()
restaurant.open_restaurant()

#9-2三家餐馆
restaurant1 = Restaurant("全聚德", "China")
restaurant1.describe_restaurant()
restaurant2 = Restaurant("无名居", "China")
restaurant2.describe_restaurant()
restaurant3 = Restaurant("Tabelog", "Japan")
restaurant3.describe_restaurant()

#9-3用户
class User:
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address

    def descibe_user(self):
        name = self.name
        print('\n'+ name + "" + self.age + "岁.")
        print("居住在" + self.address+".")

    def greet_user(self):
        name = self.name
        print("欢迎你，" + name + ".")

user1 = User('猴猴', '21', "达州")
user1.descibe_user()
user1.greet_user()
user2 = User('小胖', '20', "攀枝花")
user2.descibe_user()
user2.greet_user()
user3 = User('小向', '20', "射洪")
user3.descibe_user()
user3.greet_user()

