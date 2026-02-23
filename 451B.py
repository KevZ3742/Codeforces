# B. Sort the Array
# https://codeforces.com/problemset/problem/451/B
# 1300

n = int(input())
a = list(map(int, input().split()))

target = sorted(a)

if a == target:
    print("yes")
    print("1 1")
    exit()

l = 0
r = n - 1
while a[l] == target[l]:
    l += 1

while a[r] == target[r]:
    r -= 1   

if a[:l] + a[l:r + 1][::-1] + a[r + 1:] == target:
    print("yes")
    print(l + 1, r + 1)
    exit()
else:
    print("no")