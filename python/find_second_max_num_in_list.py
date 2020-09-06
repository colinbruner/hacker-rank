# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
# COMPLETE

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    arr.reverse()
    for i in range(n):
        if arr[i] != arr[i + 1]:
            print(arr[i + 1])
            break
