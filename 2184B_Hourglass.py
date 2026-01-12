# https://codeforces.com/contest/2184/problem/B
# rating: ?

t = int(input())

for _ in range(t):
    s, k, m = map(int, input().split())

    flips = m // k
    toPrint = 0

    if flips % 2 == 0:
        toPrint = s - m % k
    else:
        toPrint = min(s, k) - m % k

    if toPrint < 0:
        print(0)
    else:
        print(toPrint)
    
        
    