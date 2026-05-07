# B. Fancy Coins
# https://codeforces.com/problemset/problem/1860/B
# rating: 1200

t = int(input())

for _ in range(t):
    m, k, a1, ak = map(int, input().split())

    m -= min(ak, m // k) * k
    m -= min(a1, m)

    if m == 0:
        print(0)
        continue

    if a1 >= abs(m - (m // k + 1) * k) and m % k != 0:
        m += k - m % k

    toPrint = m // k
    m -= toPrint * k
    toPrint += m

    print(toPrint)