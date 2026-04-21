def genSpiral(n):
    positions = {}
    positions[(0, 0)] = 1
    if n == 1:
        return positions

    r, c = 1, 0
    num = 2
    positions[(r, c)] = num
    num += 1

    k = 1
    while num <= n:
        for _ in range(k - 1):
            if num > n: break
            r, c = r + 1, c + 1
            positions[(r, c)] = num
            num += 1

        for _ in range(k):
            if num > n: break
            r, c = r - 1, c + 1
            positions[(r, c)] = num
            num += 1

        for _ in range(k):
            if num > n: break
            r, c = r - 1, c - 1
            positions[(r, c)] = num
            num += 1

        for _ in range(k):
            if num > n: break
            r, c = r + 1, c - 1
            positions[(r, c)] = num
            num += 1

        if num <= n:
            r, c = r + 1, c
            positions[(r, c)] = num
            num += 1

        k += 1

    return positions

def buildGrid(positions, ring=False):
    pCells = set(positions.keys())

    oCells = set()
    if ring:
        for (r, c) in pCells:
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                neighbor = (r + dr, c + dc)
                if neighbor not in pCells:
                    oCells.add(neighbor)

    allCells = pCells | oCells
    rows = [r for r, c in allCells]
    cols = [c for r, c in allCells]
    min_r, max_r = min(rows), max(rows)
    min_c, max_c = min(cols), max(cols)
    height = max_r - min_r + 1
    width = max_c - min_c + 1

    grid = [['.' for _ in range(width)] for _ in range(height)]

    for (r, c) in pCells:
        grid[r - min_r][c - min_c] = 'P'

    for (r, c) in oCells:
        grid[r - min_r][c - min_c] = 'O'

    return grid

def printGrid(grid):
    print(len(grid), len(grid[0]))
    for row in grid:
        print(''.join(row))

a = int(input())
positions = genSpiral(a)
grid = buildGrid(positions, ring=True)
printGrid(grid)