# https://www.hackerrank.com/challenges/angry-professor/problem
# COMPLETE

def angryProfessor(k, a):
    on_time = 0
    for student in a:
        if student <= 0:
            on_time += 1

    if on_time >= k:
        return "NO"
    else:
        return "YES"
