while_check=True

while while_check:
    number = input("pls input how many numbers for average:")
    
    try:
        number = int(number)
        while_check = False
    except:
        print("it must be a number")
        
sum = 0
for i in range(number):
    value =  input("Enter a number:")
    sum += float(value)
    
print("the average of the " + str(number) + " numbers is: " + str(sum / number))
print(f"the average is{sum/number}")