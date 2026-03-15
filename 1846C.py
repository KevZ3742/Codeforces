# C. Rudolf and the Another Competition
# https://codeforces.com/problemset/problem/1846/C
# rating: 1200

t = int(input())

for _ in range(t):
    n, m, h = map(int, input().split())

    scores = []

    for line in range(n):
        a = sorted(map(int, input().split()))

        solved = 0
        penalty = 0

        timer = 0
        for time in a:
            if time + timer > h:
                break

            timer += time
            penalty += timer
            solved += 1

        scores.append((-solved, penalty, line))

    scores.sort()

    for i, score in enumerate(scores):
        if score[2] == 0:
            print(i + 1)
            break