# A. Medium Number
# https://codeforces.com/problemset/problem/1760/A
# rating: 800

t = int(input())

for _ in range(t):
    a = list(map(int, input().split()))
    
    a.remove(max(a))
    a.remove(min(a))
    
    print(*a)