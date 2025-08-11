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
    pick_balls = ball_list[:ballnum] #the first 7 numbers in the shuffled list
    return pick_balls
    
print(f"pick 7 lucky numbers from 1 to 35:{picknumbers(35, 7)}")
print("the win number is:" + str(picknumbers(20, 1)))

#git chekout -b work_shop4_frank
#git branch --set-upstream-to=origin/Frank-workshop_4 Frank-workshop_4
#git pull
#git commit -m "dfdfdfd"
#git push