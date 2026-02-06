# rating: 800

t = int(input())

for _ in range(t):
    n = int(input())

    toPrint = ""
    for i in range(1, n + 1):
        toPrint += str(i) + " "

    print(toPrint)