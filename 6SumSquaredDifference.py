import math


def __main__():
    sumSquared = math.pow(100*(100+1)/2, 2)
    squaredSum = 0
    for i in range(0, 101):
        squaredSum += pow(i, 2)
    print(squaredSum - sumSquared)



if __name__ == '__main__':
    __main__()
