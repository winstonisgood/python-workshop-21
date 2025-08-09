while_check=True
number_list = []

while while_check:
    number = input("pls input number into the array:")
    
    try:
        number = float(number)
        number_list.append(number)
    except:
        print("it is not a number, entering termitated")
        break

number_list.sort()

for i in number_list:
    print(i)

print("Totally "+ str(len(number_list)) + " numbers you inputed" +"\n"+
      "the max one is: " + str(number_list[-1]) + "\n"+
      "the min one is: " + str(number_list[0]) + "\n"+
      "the average is: " + str(sum(number_list) / len(number_list))   
)
