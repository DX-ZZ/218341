# 8-12三明治
import color as color


def make_sandwich(*foods):
    print("\ncustomer accept add in sandwich with the following foods:")
    for food in foods:
        print("-" + food)


make_sandwich('cake')
make_sandwich('生菜', '火腿', 'cheese')


# 8-13用户简介
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('潇', '邓',
                             location='四川省',
                             like='game',
                             sport='羽毛球')
print(user_profile)


# 8-14汽车
def car(manufacturers, size, **user_inf):
    profile = {}
    profile['brand'] = manufacturers
    profile['type'] = size
    for key, value in user_inf.items():
        profile[key] = value
    return profile


user=car('subaru', 'outback',
        颜色='blue',
        油耗='high',加速='fast')
print(user)
