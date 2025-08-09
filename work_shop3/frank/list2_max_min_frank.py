while_check=True
number_list = []

while while_check:
    number = input("pls input number into the array:")
    
    try:
        number = float(number)
        number_list.append(number)
    except ValueError:
        print("it is not a number, entering termitated")
        break

i = 0
max_number = 0
min_number = 0
max_index = 0
min_index = 0

for single_number in number_list:
    if i == 0 :
        max_number = min_number = single_number
        max_index = min_index = number_list.index(single_number)
    i += 1
    
    if max_number < single_number:
        max_number = single_number
        max_index = number_list.index(single_number)
    if min_number > single_number:
        min_number = single_number
        min_index = number_list.index(single_number)
    
print(
    "In these " + str(len(number_list)) + " numbers you inputed totally: " + str(sum(number_list)) + "\n" +
    "the max one is: " + str(max_number) + " at index: " + str(max_index) + "\n" +
    "the min one is: " + str(min_number) + " at index: " + str(min_index) + "\n" +
    "the average is: " + str(sum(number_list) / len(number_list)) 
    )   

# number_list.sort()

# for i in number_list:
#     print(i)

# print("Totally "+ str(len(number_list)) + " numbers you inputed" +"\n"+
#       "the max one is: " + str(number_list[-1]) + "\n"+
#       "the min one is: " + str(number_list[0]) + "\n"+
#       "the average is: " + str(sum(number_list) / len(number_list))   
# )
