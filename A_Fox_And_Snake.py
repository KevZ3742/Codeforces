# rating: 800

n, m = map(int, input().split())

toPrint = []
for i in range(n):
    if i % 2 == 0:
        toPrint.append("#" * m)
        continue

    if i // 2 % 2 == 0:
        toPrint.append("." * (m - 1) + "#")
    else:
        toPrint.append("#" + "." * (m - 1))

for row in toPrint:
    print(row)