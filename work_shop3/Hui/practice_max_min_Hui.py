# Calculate max, min, total, average (advance)
# Create a python file exercise3.py allow user to find 
# max and min number and the index of that number, 
# total and average number from a group of numbers, 
# the max number can have duplication in multiple position

# You need let people enter the number again if user didn't enter a number
# To achieve this you need use a list, if else condition, 
# while and for loops, isdecimal() print() input() str() float() methods. 
# Please make sure all the number people entered is stored in a list.

# ### Example Output
# ```bash
# Please enter how many number you going to enter: d
# The text you entered is not a number!
# Exaomple:
# Please enter how many number you going to enter: 3
# please enter a number: 23
# please enter a number: 23
# please enter a number: 18.9
# Output:
# The max number is 23 and position at 0,1
# The min number is 18.9 and position at 2
# The total is 64.9
# The average number is 24.96666666667
# ```

"""
practice to use try and except to check user input and error handling
try block will try to execute the code in the block
if there is an error, it will jump to except block
and execute the code in except block
"""

"""
this is a while check to make sure user enter a number
if user enter a text, it will keep asking user to enter a number
"""

"""
this is a for loop to let user enter the number,
and store the number in a list.
also check the user enter a valid number,
if user enter a text, it will ask user to enter a number again.
"""

"""
break and continue statement
break statement will exit the loop
continue statement will skip the current iteration and go to the next iteration
"""

"""
at the first time, I use try except to check user input and value is valid or not.
the second time, I add break and continue to inhance the lope logic practice.
"""

"""
some hints of break and continue just for me:
break exit the loop,
continue skip the current iteration and go to the next iteration.
"""

while_check=True
while while_check:
    quantity = input('Please enter how many numbers you going to enter:')
    try:
        quantity = int(quantity)
        while_check = False
        break
    except:
        print("The text you entered is not a number!")
        continue

"""
this block should have a while loop to check user input too
otherwise, if user enter a text, it will cause error,
because of the error input will take one try in for i in range loop
"""
number_list = []
for i in range(quantity):
    number_check = True
    while number_check:
        value = input("Please enter a number:")
        try:
            value = float(value)
            number_check = False
            break
        except:
            print("Please enter a valid number!")
            continue
    number_list.append(value)

"""
print the list of number
calculate the max, min, total, average value
and find the index of max and min number
"""

print(number_list)
max_value = max(number_list)
min_value = min(number_list)
total = sum(number_list)
average = total / quantity

max_index = []
for i in range(quantity):
    if number_list[i] == max(number_list):
        max_index.append(i)

min_index = []
for i in range(quantity):
    if number_list[i] == min(number_list):
        min_index.append(i)

"""
print the result"""
print(f"The max number is {max_value} and position at {max_index}")
print(f"The min number is {min_value} and position at {min_index}")
print(f"The total is {total}")
print(f"The average number is {average}")