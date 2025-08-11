import random # Random module for shuffling

def picknumbers(poolsize, ballnum):
    """
    Function to pick a specified number of unique balls from a pool.
    :param poolsize: Total number of balls in the pool. 
    :param ballnum: Number of balls to pick from the pool.
    :return: A list of unique balls picked from the pool.
    """
    balls = list(range(1, poolsize + 1)) # Create a list of balls numbered from 1 to poolsize
    
    random.shuffle(balls) # Shuffle the list of balls to ensure randomness
    
    if not isinstance(poolsize, int) or not isinstance(ballnum, int):
        raise TypeError("Both poolsize and ballnum must be integers.")
    if poolsize < 1:
        raise ValueError("Pool size must be at least 1.")
    if ballnum < 1:
        raise ValueError("Number of balls to pick must be at least 1.")
    if ballnum > poolsize:
        raise ValueError("Number of balls to pick cannot be greater than pool size.")
    
    picked = balls[:ballnum] # Pick the first 'ballnum' balls from the shuffled list
    
    return picked # Return the list of picked balls

winning_numbers = picknumbers(35, 7) # Usage of the function to pick 7 balls from a pool of 35

powerball_numbers = picknumbers(20, 1) # Usage of the function to pick 1 ball from a pool of 20

print("Winning Numbers:", winning_numbers, "Powerball Number:", powerball_numbers) # Print the winning numbers and powerball number
