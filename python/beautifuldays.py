# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem
# COMPLETE


def beautifulDays(i, j, k):
    beautiful_days = 0
    for day in range(i, j + 1):
        if (day - int(str(day)[::-1])) % k == 0:
            beautiful_days += 1

    return beautiful_days


print(beautifulDays(20, 23, 6))
