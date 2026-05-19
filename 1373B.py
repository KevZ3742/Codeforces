# B. 01 Game
# https://codeforces.com/problemset/problem/1373/B
# rating: 900

t = int(input())

for _ in range(t):
    s = input()

    if min(s.count("0"), s.count("1")) % 2:
        print("DA")
    else:
        print("NET")