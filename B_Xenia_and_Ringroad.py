# rating: 1000

n, m = map(int, input().split())
a = list(map(int, input().split()))

house = 1
time = 0

for task in a:
    if task >= house:
        time += task - house
    else:
        time += n - house + task

    house = task

print(time)