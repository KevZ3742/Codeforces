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
    for i in range(1, int(n ** .5) + 1):
        if n % i == 0:
            periods.append(i)
            if i != n // i:
                periods.append(n // i)
    periods.sort()

    for p in periods:
        flag = True
        toPrint = []

        for i in range(p):
            common = set.intersection(*cols[i:n:p])
            
            if not common:
                flag = False
                break

            toPrint.append(next(iter(common)))

        if flag:
            print("".join(toPrint) * (n // p))
            break