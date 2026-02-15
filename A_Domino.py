# rating: 1200

n = int(input())

oddx = oddy = pairs = 0
for _ in range(n):
    x, y = map(int, input().split())

    if x % 2 and y % 2:
        pairs += 1
        oddx += 1
        oddy += 1
    elif x % 2:
        oddx += 1
    elif y % 2:
        oddy += 1

if oddx % 2 == 0 and oddy % 2 == 0:
    print(0)
elif oddx % 2 == 1 and oddy % 2 == 1 and (pairs != oddx or pairs != oddy):
    print(1)
else:
    print(-1)