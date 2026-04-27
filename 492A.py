# A. Vanya and Cubes
# https://codeforces.com/problemset/problem/492/A
# rating: 800

n = int(input())

height = 0
cubesUsed = 0
while cubesUsed <= n:
    height += 1
    cubesUsed += (height * (height + 1)) // 2

print(height - 1)