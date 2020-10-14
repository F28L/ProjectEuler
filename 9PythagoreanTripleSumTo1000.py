import time

start = time.time()
for a in range(1, 999):
    for b in range(1, 999):
        c = 1000 - (a + b)
        if a * a + b * b == c * c:
            # this is a pyth triple
            if a + b + c == 1000:
                print(a*b*c)
                print("This code took: " + str((time.time() - start)) + " seconds")
