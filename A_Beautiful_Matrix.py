# 800

moves = 0
for i in range(5):
    row = list(map(int, input().split()))

    for j in range(5):
        if row[j] == 1:
            moves = abs(2 - j) + abs(2 - i)
            break

print(moves)