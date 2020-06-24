filename = 'guest_book.txt'

while True:
    name = input('Enter your name:')
    with open(filename, 'a') as file_object:
        file_object.write(name + '\n')
        print(f'welcome!{name.title()}')