# rating: ?

t = int(input())

for _ in range(t):
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))

    transfers = 0
    for bank in a:
        transfers += bank // x

    total = 0
    for bank in a:
        curr = bank + (transfers - bank // x) * y
        total = max(total, curr)

    print(total)