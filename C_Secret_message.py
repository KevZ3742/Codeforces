# rating: ?

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    
    rows = []
    for line in range(k):
        rows.append(input())

    cols = []
    for i in range(n):
        col = set()
        for row in rows:
            col.add(row[i])
        cols.append(col)

    periods = []
    for i in range(1, n + 1):
        if n % i == 0:
            periods.append(i)

    for p in periods:
        flag = True
        toPrint = ""

        for j in range(p):
            group = []
            for i in range(j, n, p):
                group.append(cols[i])

            common = set.intersection(*group)
            
            if not common:
                flag = False
                break

            toPrint += next(iter(common))

        if not flag:
            continue

        print(toPrint * (n // p))
        break

# tle