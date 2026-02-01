# rating: 1100

n, m, c = input().split()
n, m = int(n), int(m)

room = []
for _ in range(n):
    room.append(list(input()))

deputies = set()

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for row in range(n):
    for col in range(m):
        if room[row][col] == c:
            for dr, dc in dirs:
                nr, nc = row + dr, col + dc
                if 0 <= nr < n and 0 <= nc < m:
                    neighbor = room[nr][nc]
                    if neighbor != "." and neighbor != c:
                        deputies.add(neighbor)

print(len(deputies))