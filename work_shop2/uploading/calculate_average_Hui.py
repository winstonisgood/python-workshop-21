# 2.  Calculate average

# - Create a python file average.py allow user to find average number from a group of numbers
# - You need let people enter the number again if user didn't enter a number
# - To achieve this you need use a list, if else condition, while and for loops, isdecimal() print() input() str() float() methods

# ### Example Output

# ```bash
# Please enter how many number you going to enter: d
# The text you entered is not a number!

# Please enter how many number you going to enter: 3
# please enter a number: 23
# please enter a number: 23
# please enter a number: 18.9

# The average number is 21.633333333333336

d=input("Please enter how many number you going to enter: ")
while not d.isdecimal():
    print("The text you entered is not a number!")
    d=input("Please enter how many number you going to enter: ")
d=int(d)
number_list=[]
for i in range(d):
    n=input("please enter a number: ")
    while True:
        try:
            n=float(n)
            break
        except:
            print("The text you entered is not a number!")
            n=input("please enter a number: ")
    number_list.append(n)
average=sum(number_list)/d
print("The average number is",average)