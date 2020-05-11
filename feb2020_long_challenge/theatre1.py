t = int(input())

def l_remove(l, ind):
    tmp = []
    for i in range(len(l)):
        if i not in ind:
            tmp.append(l[i])
    return tmp

maintain = 0
for i in range(t):
    expen = 0
    table = [[0 for i in range(4)] for i in range(4)]
    n = int(input())
    kp = [100, 75, 50, 25]
    z = 0
    for j in range(n):
        l = input().split()
        movie = l[0]
        time = int(l[1])
        if movie == 'A' and time == 12:
            table[0][0] += + 1
        elif movie == 'A' and time == 3:
            table[0][1] += 1
        elif movie == 'A' and time == 6:
            table[0][2] += 1
        elif movie == 'A' and time == 9:
            table[0][3] += 1
        elif movie == 'B' and time == 12:
            table[1][0] += 1
        elif movie == 'B' and time == 3:
            table[1][1] += 1
        elif movie == 'B' and time == 6:
            table[1][2] += 1
        elif movie == 'B' and time == 9:
            table[1][3] += 1
        elif movie == 'C' and time == 12:
            table[2][0] += 1
        elif movie == 'C' and time == 3:
            table[2][1] += 1
        elif movie == 'C' and time == 6:
            table[2][2] += 1
        elif movie == 'C' and time == 9:
            table[2][3] += 1
        elif movie == 'D' and time == 12:
            table[3][0] += 1
        elif movie == 'D' and time == 3:
            table[3][1] += 1
        elif movie == 'D' and time == 6:
            table[3][2] += 1
        elif movie == 'D' and time == 9:
            table[3][3] += 1
    all_expense = list()
    for a in range(4):
        for b in range(4):
            if b != a:
                for c in range(4):
                    if c != a and c != b:
                        for d in range(4):
                            if d != a and d != b and d != c:
                                tmp = 0
                                for z in range(len(sorted([m1, m2, m3, m4]))):
                                    tmp = kp[z] * sorted([m1, m2, m3, m4])[z]
                                all_expense.append(tmp)
                            else:
                                continue
                    else:
                        continue
            else:
                continue
    expen = max(all_expense)
    print(expen)
    maintain = maintain + expen
print(maintain)
