# 7-8熟食店
sandwich_orders = ['egg', 'fruit', 'vegetable']
finished_sandwiches = []
while sandwich_orders:
    current_user = sandwich_orders.pop()
    print("I made your tuna sandwich: " + current_user.title())
    finished_sandwiches.append(current_user)
print("\nfinished_sandwiches:")
for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche.title())

# 7-9五香烟熏牛肉（pastrami）卖完了
sandwich_orders = ['pastrami', 'pastrami', 'dog', 'goldfish', 'pastrami', 'fruit', 'vegetable']
print("所有的pastrami被卖完了")
while 'pastram' in sandwich_orders:
    sandwich_orders.remove('pastram')
for sandwich in sandwich_orders:
    print(sandwich)

    # 7-10梦想的度假胜地
    place = {}
    flag = True
    while flag:
        name = input("你叫啥名？")
        places = input("If you could visit one place in the world, where would you go?")
        place[name] = places
        answer = input("是否继续?（yes/no）")
        if answer == 'no':
            flag = False
            print("结束！")
            for name, places in place.items():
                print(name, "want to go to", place)
