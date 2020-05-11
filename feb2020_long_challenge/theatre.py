t = int(input())

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
    for x in range(4):
        maxi = -1
        ind = -1
        row = -1
        for y in range(4):
            # if maxi <= max(table[y]):
                # maxi = max(table[y])
            if maxi <= max(table[0][y], table[1][y], table[2][y], table[3][y]):
                maxi = max(table[0][y], table[1][y], table[2][y], table[3][y])
                # ind = table[y].index(maxi)
                ind = [table[0][y], table[1][y], table[2][y], table[3][y]].index(maxi)
                row = y
        if maxi is not 0:
            expen += maxi * kp[z]
            table[0][row] = -1
            table[1][row] = -1
            table[2][row] = -1
            table[3][row] = -1
            table[ind][0] = -1
            table[ind][1] = -1
            table[ind][2] = -1
            table[ind][3] = -1
            z = z + 1
    if z is not 4:
        expen -= (4 - z) * 100
    print(expen)
    maintain = maintain + expen
print(maintain)
