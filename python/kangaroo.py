#!/usr/bin/env python3

# https://www.hackerrank.com/challenges/kangaroo/problem
# COMPLETE

class Kangaroo:
    def __init__(self, start, jump_distance):
        self.position = start
        self.jump_distance = jump_distance

    def jump(self):
        self.position += self.jump_distance


def kangaroo(x1, v1, x2, v2):
    # Allow for 10,000 iterations as per defined constraints
    iterations = 0
    # Kangaroo 1 -> Start + first jump
    k1 = Kangaroo(x1, v1)
    # Kangaroo 2 -> Start + first jump
    k2 = Kangaroo(x2, v2)
    while iterations < 10000:
        # Break if condition is hit
        if k1.position == k2.position:
            return "YES"
        else:
            # Jumping
            k1.jump()
            k2.jump()
            iterations += 1

    return "NO"


if __name__ == "__main__":

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)
    print(result)
