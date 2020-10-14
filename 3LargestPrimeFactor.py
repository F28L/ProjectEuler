import math


def __main__():
    i = int(math.sqrt(600851475143))
    max = 600851475143
    while i >= 2:
        if (600851475143 % i == 0) and is_prime(i):
            max = i
            break
        i -= 1
    print(max)


def is_prime(n):
    if n <= 3:
        return n > 1
    elif n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6

    return True


if __name__ == '__main__':
    __main__()
