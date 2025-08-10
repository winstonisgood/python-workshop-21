# # exercise3.py

# numbers = []

# # Get how many numbers the user will enter
# while True:
#     count = input("Please enter how many number you going to enter: ")
#     if count.isdecimal():  # check if it's a valid positive integer
#         count = int(count)
#         break
#     else:
#         print("The text you entered is not a number!")

# # Get the numbers from the user
# for i in range(count):
#     while True:
#         num_str = input("please enter a number: ")
#         try:
#             num = float(num_str)  # convert to float to allow decimals
#             numbers.append(num)
#             break
#         except ValueError:
#             print("That is not a valid number! Please try again.")

# # Find max and min
# max_num = max(numbers)
# min_num = min(numbers)

# # Find positions (indexes) of max and min
# max_positions = [i for i, val in enumerate(numbers) if val == max_num]
# min_positions = [i for i, val in enumerate(numbers) if val == min_num]

# # Calculate total and average
# total = sum(numbers)
# average = total / len(numbers)

# # Output results
# print(f"\nThe max number is {max_num} and position at {','.join(map(str, max_positions))}")
# print(f"The min number is {min_num} and position at {','.join(map(str, min_positions))}")
# print(f"The total is {total}")
# print(f"The average number is {average}")






number = []
while_check = True

while while_check:
    try:
        number = input("Please enter how many number you going to enter: ")
        number = int(number)
        while_check = False #break

    except:
        print("The text you entered is not a number!")

values = []
for i in range(number):
    value = input('please enter a number: ')
    values.append(float(value))

max_value = max(value)
min_value = min(value) 
index_max = []
index_min = []

for i in range(len(value)):
    if value[i] ==max_value:
        index_max.append(i)
    if value[i] ==min_value:
        index_min.append(i)

print(f"The max number is {max_value} and position at {index_max}")
print(f"The min number is {min_value} and position at {index_min}")
print(f"The average number is {sum (values)/ len(values)}")
print(f"The average number is {sum (values)}")

    
        

# sum = 0
# for i in range(number):
#     value = input("please enter a number: ")
#     sum += float(value) # sum = sum + float(value)


# max_number = max(number)
# min_number = min(number)

# max_positions = [i for i, val in enumerate(number) if val == max_number]
# min_positions = [i for i, val in enumerate(number) if val == min_number]



# print(f"The max number is {max_number} and position at {','.join(map(str, max_positions))}")
# print(f"The min number is {min_number} and position at {','.join(map(str, min_positions))}")


# print(f"The average number is {sum / number}")


# print(f"The total is {sum}")







