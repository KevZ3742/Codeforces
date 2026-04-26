# A. A Wonderful Contest
# https://codeforces.com/contest/2222/problem/A
# rating: ?

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    if 100 in a:
        print("Yes")
    else:
        print("No")