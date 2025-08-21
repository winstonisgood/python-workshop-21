import random
def pick_numbers():
    #generate blueball numbers
    blueball = list(range(1,35))
    #shuffle the numbers randomly
    random.shuffle(blueball)
    #pick the first 7 numbers after shuffling
    pickblueball = blueball[:7]
    #pick a powerball nubmer
    powerball = random.randint(1,20)
    return pickblueball,powerball
blueball_numbers,powerball_number = pick_numbers() 
print(f"Winning Balls are: {blueball_numbers} , Powerball is: {powerball_number}")