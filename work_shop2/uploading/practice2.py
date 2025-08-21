# 2.  Calculate average
# * Create a python file average.py allow user to find average number from a group of numbers
# * You need let people enter the number again if user didn't enter a number
# * To achieve this you need use a list, if else condition, while and for loops, isdecimal() print() input() str() float() methods

# ### Example Output
# ```bash
# Please enter how many number you going to enter: d
# The text you entered is not a number!

# Please enter how many number you going to enter: 3
# please enter a number: 23
# please enter a number: 23
# please enter a number: 18.9

# The average number is 24.96666666667
while_check = True

while while_check:
    number = input("Please enter how many number you going to enter: ")

    try:
        number = int(number)
        while_check = False
    except:
        print("The text you entered is not a number!")

sum = 0
for i in range(number):
    value = input("please enter a number: ")
    sum += float(value)

print(f"The average number is {sum / number}")
