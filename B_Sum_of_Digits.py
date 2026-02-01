# rating: 1000

n = str(input())

counter = 0
while len(n) > 1:
    sum = 0
    for c in n:
        sum += int(c)
    n = str(sum)
    counter += 1

print(counter)