# https://www.hackerrank.com/challenges/validating-the-phone-number/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
#

if __name__ == "__main__":
    import re

    n = int(input())
    for _ in range(n):
        m = str(input())
        if len(m) != 10 or not re.match("^[789]", m) or not m.isdigit():
            print("NO")
        else:
            print("YES")
