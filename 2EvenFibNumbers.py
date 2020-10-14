def __main__():
    idx = 1
    sum = 0
    while fib(idx) < 4000000:
        x = fib(idx)
        if x %2 == 0:
            sum += x
        idx += 1

    print(sum)

def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)


if __name__ == '__main__':
    __main__()
