#!/usr/bin/env python3

# https://www.hackerrank.com/challenges/cut-the-sticks/problem
def cutTheSticks(arr):
    ans = []
    while arr:
        # Append len pre cut
        ans.append(len(arr))
        # Cut the sticks by min value of the arr, filter out any 0s
        arr = list(filter((0).__ne__, map(lambda x: x - min(arr), arr)))
    return ans

print(cutTheSticks([5, 4, 4, 2, 2, 8]))
