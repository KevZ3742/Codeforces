# https://codeforces.com/problemset/problem/165/A
# rating: 1000

n = int(input())

points = {}
for _ in range(n):
    x, y = map(int, input().split())

    newList = [False, False, False, False]
    for key in points.keys():
        if x == key[0]:
            if y < key[1]:
                points[key][0] = True
                newList[1] = True
            if y > key[1]:
                points[key][1] = True
                newList[0] = True

        if y == key[1]:
            if x < key[0]:
                points[key][2] = True
                newList[3] = True
            if x > key[0]:
                points[key][3] = True
                newList[2] = True

    points[(x, y)] = newList

supercentral = 0
for key in points.keys():
    if points[key] == [True, True, True, True]:
        supercentral += 1

print(supercentral)