# https://www.hackerrank.com/challenges/swap-case/problem
# COMPLETE


def swap_case(s):
    r = ""
    for c in s:
        if c.isalpha():
            r = r + c.swapcase()
        else:
            r = r + c

    return r


if __name__ == "__main__":
    s = input()
    result = swap_case(s)
    print(result)
