# https://www.hackerrank.com/challenges/input/problem
# COMPLETE

if __name__ == "__main__":
    x, k = input().split()
    p = input().replace("x", x)
    if int(k) == eval(p):
        print(True)
    else:
        print(False)
