# C. Find the Zero
# https://codeforces.com/contest/2209/problem/C
# rating: ?

t = int(input())

for _ in range(t):
    n = int(input())
    
    toPrint = -1
    
    for i in range(2, n + 1):
        print("?", 2 * i - 1, 2 * i, flush = True)
        output = int(input())

        if output:
            toPrint = 2 * i
            break
    else:
        print("?", 1, 3, flush = True)
        output = int(input())

        if output:
            toPrint = 1
        else:
            print("?", 1, 4, flush = True)
            output = int(input())

            if output:
                toPrint = 1
            else:
                toPrint = 2

    print("!", toPrint, flush = True)