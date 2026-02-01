# https://codeforces.com/problemset/problem/110/A
# rating: 800

n = input()

def isLucky(i):
    i = str(i)
    for c in i:
        if c not in "47":
            return False
    return True

count = 0
for c in n:
    if c in "47":
        count += 1

if isLucky(count):
    print("YES")
else:
    print("NO")