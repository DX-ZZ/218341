#字符串的相等和不相等
name = 'a'
print("if name = 'a' I think is true")
print(name == 'a')
print("if name = 'd' I think is false")
print(name == 'd')
print("if name = 'A' I think is false")
print(name == 'A')

#使用函数lower的测试
name = 'E'
name.lower() == 'e'

name = 'E'
name.lower() == 'E'
print(name)

#检查两个数字相等、不等、大于、小于、大于等于和小于等于
num1 = '10'
num2 = '12'
print("数字相等")
print(num1 == '10')
print("数字不等")
print(num1 != num2)
print("数字大于")
print(num2 > num1)
print("数字小于")
print(num1 < num2)
print("数字大于等于")
print(num2 >= num1)
print("数字小于等于")
print(num1 <= num2)

#使用关键字 and 和 or 的测试
TV1_num = 11
TV2_num = 12
print("电视1数量大于10且大于13")
print((str)(TV1_num>=10 and TV1_num>=13))
print("电视2的数量大于11或小于13")
print((str)(TV2_num>=10)or(TV2_num<=13))

#测试特定的值是否包含在列表中
cars = ['宝马', '奔驰', '悍马']
car = '宝马'
if car in cars:
 print(car.title() + ", 是我的")
#测试特定的值是否未包含在列表中
cars = ['宝马', '奔驰', '悍马']
car1 = '雪佛兰'
if car1 not in cars:
    print(car1.title() + ", 不是我的")
