# A. Odd One Out
# https://codeforces.com/problemset/problem/1915/A
# rating: 800

t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    
    if a == b:
        print(c)
    elif b == c:
        print(a)
    else:
        print(b)