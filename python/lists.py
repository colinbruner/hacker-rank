# COMPLETE
# https://www.hackerrank.com/challenges/python-lists/problem
class ListThing:
    def __init__(self):
        self.list = []

    def insert(self, i, e):
        self.list.insert(i, e)

    def print(self):
        print(self.list)

    def remove(self, e):
        self.list.remove(e)

    def append(self, e):
        self.list.append(e)

    def sort(self):
        self.list.sort()

    def pop(self):
        self.list.pop()

    def reverse(self):
        self.list.reverse()


if __name__ == "__main__":
    n = int(input())
    m = globals()["ListThing"]()
    for _ in range(n):
        l = str(input())
        if "insert" in l:
            i, e = map(int, l.split()[1:])
            getattr(m, "insert")(i, e)
        elif "remove" in l or "append" in l:
            f, e = l.split()
            getattr(m, f)(int(e))
        else:
            getattr(m, l)()
