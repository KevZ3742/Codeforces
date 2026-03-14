# C. Asuna and the Mosquitoes
# https://codeforces.com/problemset/problem/2092/C
# rating: 1200

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    odds = 0
    evens = 0

    for num in a:
        if num % 2:
            odds += 1
        else:
            evens += 1

    if odds == 0 or evens == 0:
        print(max(a))
    else:
        print(sum(a) - odds + 1)