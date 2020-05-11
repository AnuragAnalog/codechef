t = int(input())

for i in range(t):
    n = int(input())
    alist = list(map(int, input().split()))
    blist = list(map(int, input().split()))

    alist.sort()
    blist.sort()

    s = 0
    for i in range(n):
        s = s + min(alist[i], blist[i])

    print(s)