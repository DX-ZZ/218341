print("Give me two numbers and I'll add them.")
print("Enter 'q' to quit")

while True:
    first_number = input("\nFirst number:")
    if first_number == 'q':
        break
    second_number = input("Second number:")
    if second_number == 'q':
        break
    try:
        number_1 = int(first_number)
        number_2 = int(second_number)
        result = number_1 + number_2
    except ValueError as e:
        print("some input are not number.")
    else:
        print(f"The result is {result}")
