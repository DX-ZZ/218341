# 6-7人
roommate_0 = {'name': '小向', 'like': '追剧', 'address': '射洪'}
roommate_1 = {'name': '康康', 'like': '看电影', 'address': '广安'}
roommate_2 = {'name': '猴猴', 'like': '打游戏', 'address': '达州'}
people = [roommate_0, roommate_1, roommate_2]
for roommate in people:
    print(roommate['name'] + ":")
    for name, name_info in roommate.items():
        print("\t" + name + ":" + str(name_info) + ".")

# 6-8宠物
bird = {'type': '鸟', 'host': '康康'}
dog = {'type': '狗', 'host': '小向'}
cat = {'type': '猫', 'host': '章章'}
lion = {'type': '狮子', 'host': '猴猴'}
monkey = {'type': '猴子', 'host': '小胖'}
tiger = {'type': '老虎', 'host': '文文'}
pets = [bird, dog, cat, lion, monkey, tiger]
for pet in pets:
    for key, value in pet.items():
        print(key, ':', value)

# 6-9喜欢的地方
favorite_places = {
    '猴猴': ['London', 'Paris'],
    '小向': ['北京', '天津'],
    '章章': ['上海', '广州'],
    '康康': ['云南', '广西'],
}
for key, value in favorite_places.items():
    print(key, 'favorite place' + ':')
    for places in value:
        print(places)

# 6-10喜欢的数字
favorite_number = {
    '猴猴': '22222',
    '章章娃儿': '999',
    '小向': '666',
    '康康娃儿': '44444',
    '小胖': '55555'
}
for persons, nums in favorite_number.items():
    print("\n" + persons + "喜欢的数字是：")
    for num in nums:
        print("\t" + str(num))

# 6-11城市
cities = {
    '重庆': {
        'country': 'China',
        'population': '3124.32万人',
        'fact': '火锅城',
    },
    '北京': {
        'country': 'China',
        'population': '2154.00万人',
        'fact': '中国的首都',
    },
    '上海': {
        'country': 'China',
        'population': '2424.00万人',
        'fact': '魔都',
    }
}
for city, city_info in cities.items():
    print('\n' + city + ":")
    for info, value in city_info.items():
        print("\t" + info.title() + ":" + value.capitalize() + ".")
