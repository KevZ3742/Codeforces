# C. Different Differences
# https://codeforces.com/problemset/problem/1772/C
# rating: 1000
 
t = int(input())
 
for _ in range(t):
    k, n = map(int, input().split())
 
    toPrint = []
    toAppend = 1
    temp = 1
    for i in range(k):
        toPrint.append(toAppend)
        toAppend += temp
        temp += 1
 
    filler = n
    for i in range(k - 1, -1, -1):
        if toPrint[i] >= filler:
            toPrint[i] = filler
            filler -= 1
 
    print(*toPrint)