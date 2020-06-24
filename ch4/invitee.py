invitee = ['小向', '章章娃', '猴猴']

message = "今天心情好，请你们吃个饭"
print((str)(invitee)+message)
print(invitee[0]+"今天没得空，要去逛gai。")
invitee[0]="康康娃"
print((str)(invitee)+message)

invitee.insert(0,"小胖")
invitee.insert(2,"贝克汉姆")
invitee.append("梅西")
print("我还想邀请的好兄弟，他们就是："+(str)(invitee))

people = invitee.pop(0)
print('人多了坐不到，只有哦豁' + people)
people = invitee.pop(0)
print('雀儿巴适坐不到，下盘来' + people)
people = invitee.pop(0)
print('改天请你吃饭' + people)
people = invitee.pop(0)
print('给你说了坐不到，半边去耍' + people)

print(invitee[0]+'你跑不落好')
print(invitee[1]+'你跑不落好')

del invitee[0]
del invitee[0]

print(invitee)


