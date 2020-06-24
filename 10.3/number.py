while True:
    try:
        num_1 = input("请输入第一个数字：")
        num_2 = input("请输入第二个数字：")
        sum = int(num_1) + int(num_2)
        print("两个数字的和是：" + str(sum))
        break
    except ValueError:
        print("请输入纯数字。")