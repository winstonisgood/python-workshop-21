while_check=True
while while_check:
    try:
        number=input("Please enter hwo many number you going to enter:")
        number=int(number)
        while_check=False
    except:
        print('The text you entered is not a number!')

    values=[]
    for in range(number):
        value=input('please enter a number:')
        value.append(float(value))

    max_value=max(values)
    min_value=min(Values)
    index_max=[]
    index_min=[]

    for i in range(len(values)):
        if values[i]==max_value:
            index_max.append(i)
        if values[i]==min_value:
            index_min.append(i)


    print(f'The max number is {max(value)} and position at {value.in}')
    print(f'The max number is {min(value)} and position at {value.in}')
    print(f'The total is {sum(values)}')
    print(f'The average number is {sum(values)/len(values)}')
