# rating: 800

t = int(input())

for _ in range(t):
    n = input()
    n = n[::-1]

    toPrint = []
    for i in range(len(n)):
        if n[i] != "0":
            toPrint.append(n[i] + "0" * i)

    print(len(toPrint))
    print(*toPrint)