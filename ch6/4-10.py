#4-10切片
cars = ['Mercedes-Benz', 'BMW', 'Ferrari', 'Automobile Lamborghini S.p.A', 'Audi', 'Volkswagen']
print("There are the first three car in my garage:")
for car in cars[:3]:
    print(car.title())
print("There are the mid three car in my garage:")
for car in cars[2:5]:
    print(car.title())
print("There are the last three car in my garage:")
for car in cars[3:6]:
    print(car.title())

#4-11
Cars = ['Mercedes-Benz', 'BMW', 'Ferrari']
for Car in Cars:
        print(Car)
my_car = cars[:]

Cars.append('Audi')

my_car.append('Automobile Lamborghini S.p.A')

print('my favorite car are:')
for car in Cars:
    print(car)
print("this is my most expensive car:")
for car in my_car:
    print(car)

#4-12
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print('我最喜欢吃的是')
for food in my_foods:
    print(food)
print('朋友最喜欢吃的')
for food in friend_foods:
    print(food)