# A. Lucky Division
# https://codeforces.com/contest/122/problem/A
# rating: 1000

n = int(input())

def isLucky(i):
    i = str(i)
    for c in i:
        if c not in "47":
            return False
    return True

for i in range(n + 1):
    if isLucky(i) and n % i == 0:
        print("YES")
        break
else:
    print("NO")