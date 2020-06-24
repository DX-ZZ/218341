# 7-4披萨配料
print("输入披萨配料")
message = ""
while message != 'quit':
    message = input()
    if message != 'quit': 1
    print("披萨新添加配料")
print(message)
# 7-5电影票
age = input("请输入年龄")
while age != 'quit':
    age2 = int(age)
    if age2 >= 3 and age2 <= 12:
        print('%d需要$10' % age2)
    elif age2 > 12:
        print('%d需要$15' % age2)
    age = input('请确认你的年龄')
# 7-6使用while循环条件
age = input('请确认你的年龄')
flag = True
while flag:
    age2 = int(age)
    if age2 >= 3 and age2 <= 12:
        print('%d需要$10' % age2)
    elif age2 > 12:
        print('%d需要$15' % age2)
        age = input('请确认你的年龄')
        if age == 'quit':
            flag = False
            break

# 7-7
x = 1
while x > 0:
    print(x)
    x += 1
