#9-6冰淇淋小店
class Resturant():
    def __init__(self,resturant_name,cuisine_type):
        self.name = resturant_name
        self.type = cuisine_type
        self.number_served = 0
        self.flavors = ['banana', 'milk', 'apple', 'chocolate']

    def display_flavors(self):
        message = "This IceCreamStand provides icecreams of different flavors of"

        num = 0
        while num < 3:
            message += self.flavors[num] + ","
            num += 1

        message += self.flavors[3] + "."
        print(message)

class IceCreamStand(Resturant):

    def __init__(self,resturant_name, cuisine_type):
        super().__init__(resturant_name, cuisine_type)

my_icecream = IceCreamStand('aidale',10)
my_icecream.display_flavors()