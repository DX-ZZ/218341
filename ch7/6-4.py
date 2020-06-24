# 6-4词汇表2
PV = {
    'run': '运行',
    'overload': '重载',
    'override': '重写',
    'print': '输出',
    'class': '类',
    'generator': '生成器',
    'iterator': '迭代器',
    'iterable': '可迭代对象',
    'pip': '包管理工具',
    'PyPI': '公共资源库'
}
for 术语, 含义 in PV.items():
    print("\n术语: " + 术语)
    print("含义: " + 含义)
"""print("run的含义是" + PV['run'] + ".")
print("overload的含义是" + PV['overload'] + ".")
print("override的含义是" + PV['override'] + ".")
print("print的含义是" + PV['print'] + ".")
print("class的含义是" + PV['class'] + ".")
"""
# 6-5河流
river_biggest = {
    'amazon river': 'brazil',
    'changjiang river': 'china',
    'mississippi river': 'america'
}
for river in river_biggest.keys():
    print("The " + river.title() + " runs through " + river_biggest[river].title() + ".")
    print(river.title())
    for country in set(river_biggest.values()):
        print(country.title())
# 6-6调查
favorite_food = {
    '猴猴': 'apple',
    '小胖': 'banana',
    '小向': 'orange',
    '康康娃儿': 'meat',
}
friends = ['猴猴', '小胖', '小向', '康康娃儿']
for name in favorite_food.keys():
    if name in friends:
        print(name + "憨憨" + "I know you like eat " + favorite_food[name] + "!")
if '聪聪' not in favorite_food.keys():
    print("聪聪请你告诉我你喜欢吃啥？")
