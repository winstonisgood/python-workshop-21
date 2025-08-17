# import random
# a=[1,2,3,4,5,6,7]
# random.shuffle(a)
# print(a)

# print(random.randint(a:1,b:35))

import random

def picknumbers(poolsize, ballnum):
    """
    Randomly pick 'ballnum' numbers from a pool of 'poolsize' balls.
    Uses random.shuffle() for randomness.
    Returns a sorted list of selected numbers.
    """
    balls = list(range(1, poolsize + 1))  # create list of balls
    random.shuffle(balls)                 # shuffle them
    selected = balls[:ballnum]            # pick the first 'ballnum' balls
    return sorted(selected)               # return sorted for readability


if __name__ == "__main__":
    # Example: generate one Powerball result
    # 7 numbers from 1-35, plus 1 Powerball number from 1-20
    print("Your Powerball numbers are:")
    print(picknumbers(35, 7), picknumbers(20, 1))