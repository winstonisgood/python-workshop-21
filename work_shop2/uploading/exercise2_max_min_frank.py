i = 1;
max_number = 0
min_number = 0
total_number = 0

while True:
    input_number = input("Please enter the No." +str(i) + " number:")
    
    try:
        int_number = float(input_number)
    except ValueError:
        print("it must be a number/float for math")
        break
    
    i+=1
    if max_number < int_number:
        max_number = int_number
    if min_number > int_number:
        min_number = int_number
    total_number += int_number

print("In these "+ str(i) + " numbers you inputed totally:" + str(total_number)+"\n"+
      "the max one is :"  + str(max_number) + 
      "\n and the min one is: " + str(min_number))          

