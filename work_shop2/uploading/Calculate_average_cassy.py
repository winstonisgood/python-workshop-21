while True:
    input_value = input("Please enter how many number you going to enter:")
    try:
        int_value = int(input_value)
        break
    except:
        print("The text you entered is not a Integer number!")
        continue

value_sum = 0
for i in range (int_value):
    while True:
        float_value = input(f"please enter a number {i+1}:")
        try:
            float_number = float(float_value)
            value_sum += float_number
            break
        except:
            print("The text you entered is not a number!")
            continue
        
value_avg = value_sum / int_value
print(f"The average number is {value_avg}")
    
