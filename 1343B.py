# B. Balanced Array
# https://codeforces.com/problemset/problem/1343/B
# rating: 800

t = int(input())

for _ in range(t):
    n = int(input())

    if (n // 2) % 2:
        print("NO")
    else:
        print("YES")
        even = [*range(2, n + 1, 2)] 
        odd = [*range(1, n - 1, 2)]
        toPrint = even + odd + [sum(even) - sum(odd)]
        print(*toPrint)