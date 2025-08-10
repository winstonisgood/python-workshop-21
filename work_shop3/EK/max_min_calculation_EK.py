while_check = True

while while_check:
    number = input("Please enter how many number you are going to enter: ")

    try:
        number = int(number)
        while_check = False
    except:
        print("The text you entered is not a valid integer. Please try again.")

sum = 0
values = []
for i in range(number):
    value = input("Please enter a number: ")
    values.append(value)
    sum += float(value)

max_value = max(values)
max_indices = [i for i, v in enumerate(values) if v == max_value]

min_value = min(values)
min_indices = [i for i, v in enumerate(values) if v == min_value]

print(f"The maximum number is: {max_value} and position at {max_indices}")
print(f"The minimum number is: {min_value} and position at {min_indices}")
print(f"The total is: {sum}")
print(f"The average numbers is: ${sum / number}")