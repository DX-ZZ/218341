import json


def get_favorite_num():
    try:
        file_name = 'favorite_num.json'
        with open(file_name) as f_obj:
            favorite_num = json.load(f_obj)

    except FileNotFoundError:
        favorite_num = input("what's your favorite number?")
        file_name = 'favorite_num.json'
        with open(file_name, 'w') as f_obj:
            json.dump(favorite_num, f_obj)
        print("I will remember your number")

    else:
        print("I know your favorite number is" + favorite_num)


get_favorite_num()