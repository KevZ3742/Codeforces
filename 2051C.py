# C. Preparing for the Exam
# https://codeforces.com/problemset/problem/2051/C
# rating: 1000

t = int(input())

for _ in range(t):
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    q = list(map(int, input().split()))

    if k < n - 1:
        print("0" * m)
    elif k == n:
        print("1" * m)
    else:
        missing = n * (n + 1) // 2 - sum(q)
        print("".join("1" if x == missing else "0" for x in a))