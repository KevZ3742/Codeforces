# B. Fibonaccharsis
# https://codeforces.com/problemset/problem/1853/B
# rating: 1200

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    toPrint = 0

    for i in range(n // 2, n):
        b = n
        a = i

        ok = True

        for j in range(k - 1):
            prev = b - a
            b, a = a, prev

            if prev < 0:
                ok = False
                break
        
        if ok:
            toPrint += 1

    if k == 3:
        toPrint += 1

    print(toPrint)