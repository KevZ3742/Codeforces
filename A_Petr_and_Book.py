# rating: 1000

n = int(input())
p = list(map(int, input().split()))

day = 0
while True:
    n -= p[day]

    if n <= 0:
        break

    day += 1

    if day == 7:
        day = 0

print(day + 1)