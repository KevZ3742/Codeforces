# rating: 800

n = int(input())

toPrint = []

if n % 2 == 1:
    print(-1)
else:
    counter = 0
    for i in range(n):
        if i % 2 == 0:
            counter += 2
            toPrint.append(counter)
        else:
            toPrint.append(counter - 1)

    print(*toPrint)