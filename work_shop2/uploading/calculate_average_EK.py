while_check = True

while while_check:
    number = input("Please enter how many number you are going to enter: ")

    try:
        number = int(number)
        while_check = False
    except:
        print("Please enter a valid integer.")

sum = 0
for i in range(number):
    value = input("Please enter a number: ")
    sum += float(value)
#   sum = sum + float(value)      print("this is 2") 

print(f"The average numbers is: ${sum / number}")