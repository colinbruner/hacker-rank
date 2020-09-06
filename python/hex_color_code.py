# https://www.hackerrank.com/challenges/hex-color-code/problem
# COMPLETE

import re

n = int(input())

for _ in range(n):
    line = input()
    m = re.findall("[\s:](#[a-f0-9]{6}|#[a-f0-9]{3})", line, re.I)
    for group in m:
        print(group)
