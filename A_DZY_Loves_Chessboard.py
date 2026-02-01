# rating: 1200

n, m = map(int, input().split())

board = []

for _ in range(n):
    row = list(input())
    board.append(row)

for r in range(n):
    if r % 2 == 0:
        current = "B"
    else:
        current = "W"

    for c in range(m):
        if board[r][c] == ".":
            board[r][c] = current

        if current == "B":
            current = "W"
        else:
            current = "B"

for row in board:
    print("".join(map(str, row)))