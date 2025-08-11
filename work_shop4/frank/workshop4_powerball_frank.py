import random

def picknumbers(poolsize:int, ballnum:int) :
    """
    This function picks a set of random numbers from a pool.
    :param poolsize: The size of the pool to pick from.
    :param ballnum: The number of balls to pick.
    :return: A list of picked numbers.
    """
    ball_list =list(range(1, poolsize + 1))#initial and sort list
    random.shuffle(ball_list) #shuffle the list
    pick_balls = ball_list[:ballnum] #the first numbers in the shuffled list
    return pick_balls

def pickballs(poolsize:int, ballnum:int) -> list:
    """
    another function to pick NOT REPEAT numbers from a list.
    using random.sample to pick unique numbers.
    """
    pool_list = list(range(1, poolsize+1))  # Create a list from 1 to poolsize
    #print("pickballs pool_list:" + str(pool_list))
    
    picked_list = []  # Initialize an empty list to store picked numbers
    picked_list = random.sample(pool_list, ballnum)  # Use random.sample to pick unique numbers
    #print("picked_list:"+str(picked_list))
    
    # for i in range(ballnum):
    #     picked = random.randint(0, len(pool_list) - 1)  # Generate a random index
    #     picked_list.append(pool_list[picked])  # Append the picked number to the list
    #     #print("pool_list i="+str(i)+" picked=" +str(picked) +": " + str(pool_list))
    #     try:
    #         pool_list.remove(picked)  # Remove the picked number from the pool
    #     except ValueError:
    #         print(f"ValueError: {picked} not in pool_list, skipping removal.")
    #     i += 1
    return picked_list
        
print("pick 7 balls from 1 to 35: " + str(pickballs(35, 7)))        
#print(f"pick 7 lucky numbers from 1 to 35:{picknumbers(35, 7)}")
print("the win number is:" + str(picknumbers(20, 1)))

#git chekout -b work_shop4_frank
#git branch --set-upstream-to=origin/Frank-workshop_4 Frank-workshop_4
#git pull
#git commit -m "dfdfdfd"
#git push