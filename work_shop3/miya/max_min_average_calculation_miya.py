while_check = True

while while_check:
    number = input("Please enter how many number you going to enter: ")

    try:
        number = int(number)
        while_check = False #break
    except:
        print("The text you entered is not a number!")

sum = 0
for i in range(number):
    value = input("please enter a number: ")
    sum += float(value) # sum = sum + float(value)

print(f"The average number is {sum / number}")

