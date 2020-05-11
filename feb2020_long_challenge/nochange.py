t = int(input())

for i in range(t):
    n, p = map(int, input().split())
    coins = list(map(int, input().split()))

    exact = True
    for c in coins:
        if p%c != 0:
            exact = False
            break
    
    if exact:
        print("NO")
        continue
    else:
        print("YES", p//c+1, end=" ")
        for j in range(len(coins)-1):
            print("0", end=" ")
        print()
