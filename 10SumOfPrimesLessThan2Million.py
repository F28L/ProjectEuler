import time


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


def __main__():
    i = 2
    sum = 0
    while i < 2000000:
        if is_prime(i):
            sum += i
        i += 1
    print(sum)


if __name__ == '__main__':
    start = time.time()
    __main__()
    print("This code took: " + str((time.time() - start)) + " seconds")
