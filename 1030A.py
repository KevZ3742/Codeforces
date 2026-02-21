# A. In Search of an Easy Problem
# https://codeforces.com/contest/1030/problem/A
# rating: 800

n = int(input())
a = list(map(int, input().split()))

for i in a:
    if i == 1:
        print("HARD")
        exit()

print("EASY")