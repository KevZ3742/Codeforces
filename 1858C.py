# C. Yet Another Permutation Problem
# https://codeforces.com/problemset/problem/1858/C
# rating: 1000

t = int(input())

for _ in range(t):
    n = int(input())

    a = [0] * n
    cur = 0
    i = 1
    while i <= n:
        j = i
        
        while j <= n:
            a[cur] = j
            cur += 1
            j *= 2
        i += 2

    print(*a)