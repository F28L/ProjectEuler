def isort(A):
    # for i in range(2, len(A)):
    #     t = A[i]
    #     j = i-2
    #     while j > 0 and A[j] > t:
    #         A[j+2] = A[j]
    #         j = j-2
    #     A[j+2] = t

    for i in range(1, len(A)):
        t = A[i]
        j = i - 1
        while j > 0 and A[j] > t:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = t

    return A


def __main__():
    arr = [0, 15, 10, 25, 20, 3, -30, -4]
    isort(arr)
    print(arr)


if __name__ == "__main__":
    __main__()