i = 0;
max_number = 0
min_number = 0

while True:
    i+=1
    input_number = input("Please enter the No." +str(i) + " number:")
    try:
        int_number = float(input_number)
    except ValueError:
        print("it must be a number/float for math")
        break
    if max_number < int_number:
        max_number = int_number
    if min_number > int_number:
        min_number = int_number

print("In these "+ str(i) + " numbers you inputed, \n the max one is :" 
      + str(max_number) + "\n and the min one is: " + str(min_number))          

# float_number= 0.0
# times_number=0
# for i in range(int_number_average):
#     print("for i:", i)
#     float_number = input("Enter a number:")
#     try:
#         float_number = float(float_number)
#     except ValueError:
#         print("it must be a number to average")
#         #times_number -= 1
#         print("except time:", times_number)
#         continue
#     times_number += 1
#     print("times_number:", times_number)
#     float_number += float_number
    
# average = float_number / int_number_average
# print("The average of the "+str(times_number)+" numbers is: "+ str(average))