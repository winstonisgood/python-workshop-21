import random

def picknumbers(poolsize, ballnum):
    """
    生成一组不重复的随机号码
    
    :param poolsize: 号码池总数
    :param ballnum: 需要抽取的号码个数
    :return: 返回一个包含抽取号码的列表
    """
    numbers = list(range(1, poolsize + 1))  # 生成从1到poolsize的号码列表
    random.shuffle(numbers)  # 随机打乱号码顺序
    return numbers[:ballnum]  # 取前ballnum个号码作为抽取结果

# 示例：生成一组Powerball号码
if __name__ == "__main__":
    # 严格按照要求调用方式
    print(picknumbers(35, 7), picknumbers(20, 1))