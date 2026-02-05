# rating: 1200

t, sx, sy, ex, ey = map(int, input().split())
directions = input()

curr = [sx, sy]
target = [ex, ey]

dirs = {"W":[-1, 0], "E":[1, 0], "S":[0, -1], "N":[0, 1]}

flag = False
time = 0
for direction in directions:
    proposal = [curr[0] + dirs[direction][0], curr[1] + dirs[direction][1]]
    if abs(target[0] - proposal[0]) < abs(target[0] - curr[0]) or abs(target[1] - proposal[1]) < abs(target[1] - curr[1]):
        curr = proposal

    time += 1

    if curr == target:
        flag = True
        break

if not flag:
    print(-1)
else:
    print(time)