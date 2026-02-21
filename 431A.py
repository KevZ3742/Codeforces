# A. Black Square
# https://codeforces.com/contest/431/problem/A
# rating: 800

a = list(map(str, input().split()))
s = str(input())

calories = 0
for char in s:
    calories += int(a[int(char) - 1])

print(calories)    