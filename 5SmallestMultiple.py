import math


def __main__():
    maxInt = math.factorial(20) / math.factorial(10)
    valid = False
    i = 20
    while not valid:
        valid = True
        for j in range(11, 21):
            if i % j != 0:
                valid = False
                break
        i+=20
    print(i-20)

if __name__ == '__main__':
    __main__()
