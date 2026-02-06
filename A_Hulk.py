# rating: 800

n = int(input())

toPrint = []
for i in range(n):
    if i % 2 == 0:
        toPrint.append("I hate")
    else:
         toPrint.append("I love")
    toPrint.append("that")

toPrint[-1] = "it"

print(*toPrint)