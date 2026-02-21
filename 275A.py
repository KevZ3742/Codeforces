# A. Lights Out
# https://codeforces.com/contest/275/problem/A
# rating: 900

switches = []

for _ in range(3):
    row = list(map(int, input().split()))
    switches.append(row)

lights = [[1 for _ in range(3)] for _ in range(3)]

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)]

for r in range(len(switches)):
    for c in range(len(switches[r])):
        if switches[r][c] % 2 != 0:
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < 3 and 0 <= nc < 3:
                    lights[nr][nc] ^= 1

for row in lights:
    print("".join(map(str, row)))