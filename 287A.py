# 287A. IQ Test
# https://codeforces.com/problemset/problem/287/A
# rating: 1100

paper = []
for _ in range(4):
    paper.append(input())

for r in range(4):
    for c in range(3):
        if paper[r][c] == paper[r][c + 1]:
            if r + 1 <= 3:
                if paper[r][c] == paper[r + 1][c] or paper[r][c] == paper[r + 1][c + 1]:
                    print("YES")
                    exit()

            if r - 1 >= 0:
                if paper[r][c] == paper[r - 1][c] or paper[r][c] == paper[r - 1][c + 1]:
                    print("YES")
                    exit()

print("NO")