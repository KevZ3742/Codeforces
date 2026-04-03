# E. Beautiful Array
# https://codeforces.com/problemset/problem/2041/E
# rating: 1200

a, b = map(int, input().split())

if a == b:
    print(1)
    print(a)
    exit()

target = 3 * a

print(3)
print(target - (b + b) , b, b)