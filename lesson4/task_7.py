import math


def func_factorial(n):
    for k in range(1, n + 1):
        yield math.factorial(k)


for i in func_factorial(5):
    print(i)
