while_check = True


while while_check:
    number = input ("enter how many number you going to enter: ")

try:
    int(number)
    while_check = False
    
except:
    print("text you entered is not a number!")
    

sum = 0
for i in range (number):
    value = input ("please enter a number: ")
    sum += float(value) #sum = sum + float(value)

print (f"The average number is {sum/number}")