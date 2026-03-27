# A. Sieve of Erato67henes
# https://codeforces.com/problemset/problem/2195/A
# rating: 800

t = int(input())
 
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    if 67 in a:
        print("YES")
    else:
        print("NO")