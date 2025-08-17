number_average = input("how many numbers for average:")
try:
    int_number_average = int(number_average)
except ValueError:
    print("it must be a number for times")

float_number= 0.0
times_number=0
for i in range(int_number_average):
    print("for i:", i)
    float_number = input("Enter a number:")
    try:
        float_number = float(float_number)
    except ValueError:
        print("it must be a number to average")
        #times_number -= 1
        print("except time:", times_number)
        continue
    times_number += 1
    print("times_number:", times_number)
    float_number += float_number
    
average = float_number / int_number_average
print("The average of the "+str(times_number)+" numbers is: "+ str(average))