t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))

    coins = sum(l)%k
    print(coins)