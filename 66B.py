# B. Petya and Countryside
# https://codeforces.com/contest/66/problem/B
# rating: 1100

n = int(input())
h = list(map(int, input().split()))

maxBox = 0
prev = 0
for i in range(n):
    currMax = 1

    if i - 1 < 0 or h[i-1] > h[i]:
        prev = 0
    else:
        prev += 1
    
    currMax += prev

    currHeight = i
    while currHeight + 1 <= len(h) - 1 and h[currHeight] >= h[currHeight + 1]:
        currMax += 1
        currHeight += 1
    
    maxBox = max(maxBox, currMax)

print(maxBox)