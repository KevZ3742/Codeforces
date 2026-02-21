# A. Sereja and Dima
# https://codeforces.com/contest/381/problem/A
# Rating: 800

n = int(input())
a = list(map(int, input().split()))

sereja = 0
dima = 0

turn = False

l = 0
r = n - 1
while l <= r:
    add = 0
    if a[l] >= a[r]:
        add = a[l]
        l += 1
    else:
        add = a[r]
        r -= 1
    
    if turn == False:
        sereja += add 
    else:
        dima += add

    turn = not turn

print(sereja, dima)