
while_check = True
while while_check:
    # check the number is a valid integer
    try:
        number = input('Please enter how many number you going to enter: ')
        number = int(number)
        while_check = False
    except:
        print('The text you entered is not a number!')

values = []
for i in range(number):
    value = input('please enter a number: ')
    values.append(float(value))

max_value = max(values)
min_value = min(values)
index_max = []
index_min = []

# find the index for the max number and min number
for i in range(len(values)):
    if values[i] == max_value:
        index_max.append(i)
    if values[i] == min_value:
        index_min.append(i)


print(f'The max number is {max_value} and position at {index_max}')
print(f'The min number is {min_value} and position at {index_min}')
print(f'The total is {sum(values)}')
print(f'The average number is {sum(values) / len(values)}')
