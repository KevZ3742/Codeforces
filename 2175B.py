# B. XOR Array
# https://codeforces.com/problemset/problem/2175/B
# rating: 1300

t = int(input())

for _ in range(t):
    n, l, r = map(int, input().split())

    prefix = [*range(n + 1)]
    prefix[r] = prefix[l - 1]
    
    toPrint = []
    for i in range(1, n + 1):
        toPrint.append(prefix[i] ^ prefix[i - 1])

    print(*toPrint)