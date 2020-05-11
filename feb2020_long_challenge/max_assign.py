#!/usr/bin/python3

a = [[56,41,74,3],[0,0,2,0],[0,1,0,0],[1,0,0,0]]

def l_remove(l, ind):
    tmp = list()
    for i in range(len(l)):
        if i not in ind:
            tmp.append(l[i])
    return tmp

print(l_remove(a[0], [2,3]))