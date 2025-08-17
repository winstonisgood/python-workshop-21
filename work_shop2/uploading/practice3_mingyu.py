while True:
    try:
        count = int(input("Please enter how many number you going to enter:"))
        break
    except ValueError:
        print("The text you entered is not a number!")
number_list = []
total = 0
for i in range(count):
    while True:
        try:
            number = float(input("Please enter a number:"))
            number_list.append(number)
            total += number
            break
        except ValueError:
            print("The text you entered is not a number!")
max_number = number_list[0]
min_number = number_list[0]
max_position = 0
min_position = 0
for i in range(1,count):
    if number_list[i] > max_number:
        max_number = number_list[i]
        max_position = i
    if number_list[i] < min_number:
        min_number = number_list[i]
        min_position = i


average = total / count
print(f"The max number is {max_number:g} and position at {max_position}")
print(f"The min number is {min_number:g} and position at {min_position}")
print(f"The total is {total:g}")
print(f"The average number is {average:g}")