# A. Marathon
# https://codeforces.com/problemset/problem/1692/A
# rating: 800

t = int(input())

for _ in range(t):
    distances = list(map(int, input().split()))
    
    timur = distances[0]
    distances.sort()

    print(3 - distances.index(timur))