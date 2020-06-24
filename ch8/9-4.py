#9-4就餐人数
class Restaurant:
    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("Restaurant Name:" + self.restaurant_name.title())
        print("Cuisine Type:" + self.cuisine_type.title())

    def read_number_served(self):
        print("我们服务了" + str(self.number_served) + "人.\n")

    def set_number_served(self,number):
        self.number_served = number

    def increment_number_served(self,increment_number):
        self.number_served = self.number_served + increment_number

restaurant = Restaurant("全聚德", "China")
restaurant.describe_restaurant()
restaurant.read_number_served()

restaurant.number_served = 10
restaurant.read_number_served()

restaurant.set_number_served(20)
restaurant.read_number_served()

restaurant.increment_number_served(30)
restaurant.read_number_served()

#9-5尝试登录次数
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def greet_user(self):
        name = self.first_name.title() + "" + self.last_name.title()
        print("你好,"+ name + ".")

    def incement_login_attempts(self):
        self.login_attempts = self.login_attempts + 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user = User('bruce', 'li')
user.greet_user()

for you in range(2):
    user.incement_login_attempts()
print("You are already login " + str(user.login_attempts) + " times.")
user.reset_login_attempts()
print("Have login " + str(user.login_attempts) + " time.")