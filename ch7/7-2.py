# 7-1汽车租赁
car = input()
print("Let me see if I can find you a " + car + ".")

# 7-2餐馆定位
message = int(input("请问你们几位？"))
if message > 8:
    print("sorry，8个人以上的位置没有了。")
elif message <= 0:
    print("吃饭不能少于一人")
else:
    print("还有位置，请坐。")

# 7-3 10的整倍数
number = int(input("随机输入一个数，这个数是否是10的整倍数"))
if number % 10 ==0:
 print("你输入的数字是" + str(number) + "，是10的整倍数")
else:
 print("你输入的数字是" + str(number) + "，不是10的整倍数")
