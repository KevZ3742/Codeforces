# https://codeforces.com/problemset/problem/224/A
# rating: 1100

areas = list(map(int, input().split()))

edge1 = areas[0] * areas[1] / areas[2]
edge2 = areas[1] * areas[2] / areas[0]
edge3 = areas[2] * areas[0] / areas[1]

edge1 = edge1 ** .5
edge2 = edge2 ** .5
edge3 = edge3 ** .5

print(int(4 * (edge1  + edge2 + edge3)))