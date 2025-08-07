while True:
    input_value = input("Please enter how many number you going to enter: ")
    try:
        int_value = int(input_value)
        break
    except:
        print("The text you entered is not a Integer number!")
        continue

value_sum = 0 
float_array = []
for i in range (int_value):
    while True:
        float_value = input(f"please enter a number {i+1}:")
        try:
            float_number = float(float_value)
            value_sum += float_number
            float_array.append(float_number)
            break
        except:
            print("The text you entered is not a number!")
            continue        
print(float_array) 
max_value = max(float_array)
max_index = float_array.index(max_value)
print(f"The max number is {max_value} and position at {max_index}")
min_value = min(float_array)
min_index = float_array.index(min_value)
print(f"The min number is {min_value} and position at {min_index}")
value_avg = value_sum / int_value
print(f"The total is {value_sum}")
print((f"The average number is {value_avg}"))





