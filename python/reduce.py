from fractions import Fraction
from functools import reduce

# https://www.hackerrank.com/challenges/reduce-function/problem
# COMPLETE

def product(fracs):
    t = reduce(lambda a, b: a * b, fracs)
    return t.numerator, t.denominator


if __name__ == "__main__":
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
