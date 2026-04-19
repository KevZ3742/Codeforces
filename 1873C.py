# C. Target Practice
# https://codeforces.com/problemset/problem/1873/C
# rating: 800

t = int(input())

for _ in range(t):
    points = 0

    for i in range(10):
        arrows = input()

        for j in range(10):
            if arrows[j] == "X":
                points += min(i, j, 9 - i, 9 - j) + 1

    print(points)
