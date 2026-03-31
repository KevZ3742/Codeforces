# B. Heapify 1
# https://codeforces.com/problemset/problem/2195/B
# rating: 900

t = int(input())

for _ in range(t):
    n = int(input())
    a = [0] + list(map(int, input().split()))

    b = a[:]

    for i in range(1, n + 1, 2):
        indices = []
        j = i
        while j <= n:
            indices.append(j)
            j *= 2

        values = [b[idx] for idx in indices]
        values.sort()

        for idx, val in zip(indices, values):
            b[idx] = val

    if all(b[i] == i for i in range(1, n + 1)):
        print("YES")
    else:
        print("NO")