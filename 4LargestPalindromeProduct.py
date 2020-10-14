def is_palin(n):
    if str(n) == str(n)[::-1]:
        return True
    return False


def __main__():
    i = 999
    max = -1
    while i >= 100:
        j = 999
        while j >= 100:
            prod = i * j
            print("i = " + i.__str__())
            print("j = " + j.__str__())
            print("prod = " + prod.__str__())
            if is_palin(prod):
                if prod > max:
                    max = prod
                    print(prod)
            j -= 1
        i -= 1
    print(max)

if __name__ == '__main__':
    __main__()
