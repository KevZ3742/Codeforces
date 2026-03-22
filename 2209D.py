# D. Ghostfires
# https://codeforces.com/contest/2209/problem/D
# rating: ?

t = int(input())
 
for _ in range(t):
    r, g, b = map(int, input().split())
 
    v = sorted([('R',r),('G',g),('B',b)], key=lambda x: x[1], reverse=True)
    colorA, countA = v[0]
    colorB, countB = v[1]
    colorC, countC = v[2]
 
    countA = min(countA, countB + countC + 1)
    toPrint = ""
 
    for i in range(countB):
        if countA > 0:
            toPrint += colorA
            countA -= 1
        
        toPrint += colorB
 
    for i in range(countC):
        if countA > 0:
            toPrint += colorA
            countA -= 1
        
        toPrint += colorC
 
    if countA > 0:
        toPrint += colorA
 
    print(toPrint)

# wa