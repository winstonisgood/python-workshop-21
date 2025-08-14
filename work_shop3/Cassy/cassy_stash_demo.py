while True:
    input_value = input("Please enter how many number you going to enter: ")
    try:
        int_value = int(input_value)
        break
    except:
        print("The text you entered is not a Integer number!")
        continue






