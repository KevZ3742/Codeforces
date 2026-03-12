# B. Lady Bug
# https://codeforces.com/problemset/problem/2092/B
# rating: 1200

t = int(input())

for _ in range(t):
    n = int(input())
    a = input()
    b = input()

    zigzag1 = []
    zigzag2 = []

    for i in range(n):
        if i % 2 == 0:
            zigzag1.append(a[i])
            zigzag2.append(b[i])
        else: 
            zigzag1.append(b[i])
            zigzag2.append(a[i])

    if zigzag1.count("1") <= zigzag1.count("0") and zigzag2.count("1") <= zigzag2.count("0") + 1:
        print("YES")
    else:
        print("NO")