current_users = ['admin', 'DX', 'WGZ', 'XZY', 'WXK']
new_users = ['DMJ', 'DX', 'YC', 'John', 'WXK']
for new_user in new_users:
    if new_user in current_users:
        print(new_user+" Have used")
    else:
        print(new_user+" not use")



#5-11
nums = list(range(1,10))
for num in nums:
    if num == 1:
        print("%sst" % (num))
    elif num == 2:
        print("%snd" % (num))
    elif num == 3:
        print("%srd" % (num))
    else:
        print("%sth" % (num))
