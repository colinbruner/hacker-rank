if __name__ == "__main__":
    # x = int(input())
    # y = int(input())
    # z = int(input())
    # n = int(input())
    x = 3
    y = 3
    z = 3

    i = [i for i in range(x + 1)]
    j = [i for i in range(y + 1)]
    k = [i for i in range(z + 1)]

    list_of_lists = []

    def perm(a, k=0):
        if k == len(a):
            list_of_lists.append(a)
        else:
            for i in range(k, len(a)):
                a[i], a[k] = a[k], a[i]
                perm(a, k + 1)

    perm(i)
    list_of_lists.sort()
    print(list_of_lists)
