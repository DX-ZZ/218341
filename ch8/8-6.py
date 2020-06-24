#8-6
def city_country(city,country):
    result = city+","+country
    return result
result_list = []
cy = city_country('SH','China')
result_list.append(cy)
cy = city_country('NY','USA')
result_list.append(cy)
cy = city_country('Paris','France')
result_list.append(cy)
for c in result_list:
    print(c)

#8-7
def make_album(singer_name,album_name,singer_number=""):
    singer = singer_name
    album = album_name
    full_name = {singer:album}
    if singer_name:
        full_name["singer_number"] = singer_number
        print(singer_number)
        return full_name
favorite_album = make_album("MJ", "up town", 2)
print(favorite_album)
favorite_album = make_album("刘德华", "冰雨", singer_number=5)
print(favorite_album)

#8-8
name = "please input singer_name"
name += "(Press'a' quit):"
name1 = "please inout album_name"
name1 += "(Press'a' quit):"

def make_album(singer_name, album_name):
    full_name = {singer_name:album_name}
    return  full_name

while True:
    singer_name = input(name)
    if singer_name == "a":
        break
        album_name = input(name1)