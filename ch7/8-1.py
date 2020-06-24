# 8-1消息
def display_message():
 print("本章学习了def函数")
display_message()


# 8-2喜欢的图书
def favorite_book(title):
    print('One of my favorite books is' + title)
favorite_book('大数据导论')


# 8-3T恤
def make_shirt(size, word="我爱学习"):
    print("size:", size, "word:", word)

make_shirt("L")
make_shirt("M")
make_shirt("XL")


# 8-4大号T恤
def make_shirts(size, word='你好'):
    print("T恤的尺码是" + size + ",T恤上的文字是" + word)


make_shirts('xxl')
make_shirts('m')
make_shirts("other size", "其他文字")


# 8-5城市
def describle_city(city, country='China'):
    print(city + "is in" + country)


describle_city('北京')
describle_city('上海')
describle_city('米兰', ' 意大利')
