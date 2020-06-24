#9-7管理员
class User():

    def __int__(self, first_name, last_name, age, career, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.career = career
        self.login_attempts = login_attempts

class Admin(User):

    def __init__(self, first_name, last_name, age, career, login_attempts):
        super().__int__(first_name, last_name, age, career, login_attempts)
        self.privileges = [" can add post", " can delete", " can ban user"]

    def show_privileges(self):
        num = 0
        while num < 3:
            message = "Admin" + self.privileges[num] + "."
            num += 1
            print(message)

admin = Admin("xiang", "xiaozhi", 20, "caller", 3)
admin.show_privileges()