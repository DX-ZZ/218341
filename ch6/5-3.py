# 假设在游戏中刚射杀了一个外星人，请创建一个名为alien_color 的变量，并将其设置为'green'、'yellow'或'red'  编写一条 if 语句，检查外星人是否是绿色的；如果是，就打印一条消息，指出
alien_colors = ['green', 'red', 'yellow']
if 'green' in alien_colors:
    print('you got 5 points')
alien_colors2 = ['green', 'red', 'yellow']
if 'white' not in alien_colors:
    print("You can't get mark")

# 5-4 像练习 5-3 那样设置外星人的颜色，并编写一个 if-else 结构
alien_colors3 = ['green', 'red', 'yellow']
if 'green' in alien_colors3:
    print("You can get 5 points" + " because you shoot alien")
else:
    print("You can get 10 points" + " because you shoot other alien")


alien_colors3 = ['green', 'red', 'yellow']
if '' in alien_colors3:
    print("You can get 5 points" + " because you shoot alien")
else:
    print("You can get 10 points" + " because you shoot other alien")
