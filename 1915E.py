# E. Romantic Glasses
# https://codeforces.com/problemset/problem/1915/E
# rating: 1300

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    prefix = {0}

    curSum = 0
    for i in range(n):
        if i % 2:
            curSum -= a[i]
        else: 
            curSum += a[i]

        if curSum in prefix:
            print("YES")
            break
            
        prefix.add(curSum)
    else:
        print("NO")

# tle