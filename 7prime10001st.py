import math


def __main__():
    count = 0
    i = 2
    while count != 10001:
        if is_prime(i):
            count += 1
        i += 1
    print(i-1)

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
