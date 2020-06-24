try:
    with open("dogs.txt", 'r', encoding='utf-8') as dog:
        with open("cats.txt", 'r', encoding='utf-8') as cat:
            for d, c in zip(dog.readlines(), cat.readlines()):
                print(d)
                print(c)
except FileNotFoundError:
    # pass
    print("Not found...")
try:
    with open('book.txt', 'r', encoding='utf-8') as book:
        contents = book.read()
except IOError:
    print("The file is not exist.")
else:
    content_1 = contents.count('the')
    print("The file has " + str(content_1) + " 'the' words.")
    content_2 = contents.lower().count('the')
    print("The file has " + str(content_2) + " 'The' words.")
