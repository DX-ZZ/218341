#9-9电瓶升级
class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):

        long_name = str (self.year) + '' + self.make + '' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has  " + str(self.odometer_reading) + "miles.")

    def update_odometer(self, milegeage):
        if milegeage >= self.odometer_reading:
            self.odometer_reading = milegeage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery():

    def __init__(self, battary_size=70):
        self.battery_size = battary_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kwh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
        self.upgrate_battery()

    def upgrate_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85


class ElectricCar(Car):

    def __init__(self, make, model, year):
       super().__init__(make, model, year)
       self.battery_size = Battery()

    def describe_battery(self):
        self.battery_size.battery_size()

    def get_range(self):
        self.battery_size.get_range()

my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.get_range()
my_tesla.get_range()