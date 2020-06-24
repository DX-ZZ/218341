# 8-1消息
def display_message():
    print("本章学习了def函数")
    display_message()


# 8-2喜欢的图书
def favorite_book(title):
    print("One of my favorite books is" + title)
    favorite_book('大数据导论')


# 8-3T恤
def make_shirt(size, msg):
    print("这件衣服繁荣尺寸是" + size, "衣服上的文字是" + msg)

    make_shirt('xxL', '你好！')
