import math
def gen_prime(x=2):
    while True:
        for i in range(2, int(math.sqrt(x))+1):
            if x % i == 0:
                break
            else:
                yield x
            x += 1


i = gen_prime()
for c in range(10):
    print(next(i), end=" ")
    print("")
