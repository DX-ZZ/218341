filename = 'reasons.txt'

while True:
    reason = input("why are you like programming:")
    with open(filename, 'a') as file_object:
        file_object.write(f'{reason} \n')