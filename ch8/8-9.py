#8-9
def show_magicians(magicicans):
    for magicican in magicicans:
        print(magicican)
magicicans = ["Dynamo", "Jeff", "Jason"]
show_magicians(magicicans)

#8-10
def make_great(magic_person,change_name):
    while magic_person:
        new_name = magic_person.pop()
        new_name = " The great " + new_name
        change_name.append(new_name)

def show_magicians(change_name):
    for magicican in change_name:
        print(magicican)
magic_person = ["Dynamo", "Jeff", "Jason"]
change_name = []
make_great(magic_person, change_name)
show_magicians(change_name)

#8-11
def make_great(magic_person1, change_name):
    while magic_person1:
        new_name = magic_person1.pop()
        new_name = " The great " + new_name
        change_name.append(new_name)
    return change_name

def show_magicians(change_name):
    for magicican in change_name:
        print(magicican)

magic_person = ["Dynamo", "Jeff", "Jason"]
print(magic_person)
change_name = []
change_name = make_great(magic_person[:], change_name)
print(change_name)
show_magicians(change_name)