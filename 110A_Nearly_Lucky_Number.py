# https://codeforces.com/problemset/problem/110/A
# rating: 800

n = int(input())

def isLucky(i):
    i = str(i)
    for c in i:
        if c not in "47":
            return False
    return True

if isLucky(len(str(n))):
    print("YES")
else:
    print("NO")