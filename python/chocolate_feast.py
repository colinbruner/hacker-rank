# https://www.hackerrank.com/challenges/chocolate-feast/problem

def chocolateFeast(n, c, m):
    wrappers = 0
    candy = 0
    while n > 0:
        # Money left for candy
        if (n - c) >= 0:
            # Paid for candy
            n -= c
            # Acquired candy
            candy += 1
        else:
            # Out of money
            n = 0

    wrappers = candy
    while wrappers >= m:
        # Trade m wrappers, get 1 candy, get 1 more wrapper
        wrappers -= m
        candy += 1
        wrappers += 1

    return candy
