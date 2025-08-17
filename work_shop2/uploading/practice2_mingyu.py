while True:
    try:
        input_value = int(input("Please enter how many number you going to enter:"))
        break
    except ValueError:
        print("The text you entered is not a number!")
        continue
total = 0
for i in range(input_value):
    input_value2 = input("please enter a number:")
    try:
        total += float(input_value2)
    except ValueError:
        print("The text you entered is not a number!")
        continue

average = total / input_value
print(f"The average number is {average}")

