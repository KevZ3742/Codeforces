# rating: 1200

y, k, n = map(int, input().split())

toPrint = []
for i in range(n + 1):
    if i * k > n:
        break

    if i * k <= y:
        continue

    toPrint.append(i * k - y)

if not toPrint:
    toPrint.append(-1)

print(*toPrint)