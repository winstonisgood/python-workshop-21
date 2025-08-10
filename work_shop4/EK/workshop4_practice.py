import random

def picknumbers(poolsize, ballnum):
    balls = list(range(1, poolsize + 1))
    random.shuffle(balls)
    
    if not isinstance(poolsize, int) or not isinstance(ballnum, int):
        raise TypeError("Both poolsize and ballnum must be integers.")
    if poolsize < 1:
        raise ValueError("Pool size must be at least 1.")
    if ballnum < 1:
        raise ValueError("Number of balls to pick must be at least 1.")
    if ballnum > poolsize:
        raise ValueError("Number of balls to pick cannot be greater than pool size.")
    
    picked = balls[:ballnum]
    
    return picked

print(picknumbers(35, 7), picknumbers(20, 1))
