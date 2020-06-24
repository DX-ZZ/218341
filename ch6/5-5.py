# 5-5将练习 5-4 中的 if-else 结构改为 if-elif-else 结构
alien_colors4 = ['green', 'red', 'yellow']
if 'green' in alien_colors4:
    print("You can get 5 points" + " because you shoot this green alien")
elif 'yellow' in alien_colors4:
    print("You can get 10 points" + " because you shoot this yellow alien")
else:
    print("You can get 15 points" + " because you shoot this red alien")

alien_colors0 = ['green', 'red', 'yellow']
if 'white' in alien_colors0:
    print("You can get 5 points" + " because you shoot this green alien")
elif 'yellow' in alien_colors0:
    print("You can get 10 points" + " because you shoot this yellow alien")
else:
    print("You can get 15 points" + " because you shoot this red alien")

alien_colors5 = ['green', 'red', 'yellow']
if '' in alien_colors5:
    print("You can get 5 points" + " because you shoot this green alien")
elif '' in alien_colors5:
    print("You can get 10 points" + " because you shoot this yellow alien")
else:
    print("You can get 15 points" + " because you shoot this red alien")