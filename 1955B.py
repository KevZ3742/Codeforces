# B. Progressive Square
# https://codeforces.com/problemset/problem/1955/B
# rating: 1000

t = int(input())

for _ in range(t):
    n, c, d = map(int, input().split())
    b = sorted(map(int, input().split()))

    a = b[0]
    generated = []

    for i in range(n):
        for j in range(n):
            generated.append(a + i * c + j * d)

    generated.sort()

    if generated == b:
        print("YES")
    else:
        print("NO")