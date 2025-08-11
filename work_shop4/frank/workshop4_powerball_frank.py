import random

def picknumbers_1(poolsize:int, ballnum:int) :
    """
    This function picks a set of random numbers from a pool.
    :param poolsize: The size of the pool to pick from.
    :param ballnum: The number of balls to pick.
    :return: A list of picked numbers.
    """
    pool_list =list(range(1, poolsize + 1))#initial and sort list
    random.shuffle(pool_list) #shuffle the list
    picked_list = pool_list[:ballnum] #the first numbers in the shuffled list
    return picked_list

def picknumbers_2(poolsize:int, ballnum:int) -> list:
    pool_list = list(range(1, poolsize + 1))  # Create a list from 1 to poolsize
    picked_list = []  # Initialize an empty list to store picked numbers
    picked_list = random.sample(pool_list, ballnum)  # Use random.sample to pick unique numbers
    return picked_list

def picknumbers_3(poolsize:int, ballnum:int) -> list:
    # another function to pick NOT REPEAT numbers from a list.
    # remove the picked number from the pool to avoid repetition in the loop picking.

    pool_list = list(range(1, poolsize+1))  # Create a list from 1 to poolsize
    picked_list = []  # Initialize an empty list to store picked numbers
    
    for i in range(ballnum):
        picked = random.choice(pool_list)  # Generate a random index
        picked_list.append(picked)  # Append the picked number to the list
        
        try:
            pool_list.remove(picked)  # Remove the picked number from the pool
        except ValueError:
            print(f"ValueError: {picked} not in pool_list, skipping removal.")
        i += 1
        
    return picked_list
        
print("pick 7 balls from 1 to 35: " + str(picknumbers_2(35, 7)))        
print(f"pick 7 lucky numbers from 1 to 35:{picknumbers_3(35, 7)}")
print("the win number is:" + str(picknumbers_1(20, 1)))

#git chekout -b work_shop4_frank
#git branch --set-upstream-to=origin/Frank-workshop_4 Frank-workshop_4
#git pull
#git commit -m "dfdfdfd"
#git push