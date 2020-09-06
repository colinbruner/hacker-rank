# COMPLETE
# https://www.hackerrank.com/challenges/map-and-lambda-expression/problem

cube = lambda x: x ** 3  # complete the lambda function


# Weird limitation of the problem statement
def fibonacci(n):
    def fib(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)

    return [fib(i) for i in range(0, n)]


if __name__ == "__main__":
    n = int(input())
    # print(list(map(cube, [fibonacci(i) for i in range(0, n)])))
    print(list(map(cube, fibonacci(n))))
