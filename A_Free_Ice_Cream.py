# rating: 800

n, x = map(int, input().split())

distress = 0
for _ in range(n):
    operation, d = map(str, input().split())
    d = int(d)

    if operation == "-":
        if x >= d:
            x -= d
        else:
            distress += 1
    else:
        x += d

print(x, distress)