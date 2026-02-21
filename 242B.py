# B. Big Segment
# https://codeforces.com/contest/242/problem/B
# rating: 1100

n = int(input())

segments = []
points = []
for _ in range(n):
    l, r = map(int, input().split())

    points.append(l)
    points.append(r)
    segments.append((l, r))

points.sort()

if (points[0], points[-1]) in segments:
    print(segments.index((points[0], points[-1])) + 1)
else:
    print(-1)