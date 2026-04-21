# A. Mishka and Game
# https://codeforces.com/problemset/problem/703/A
# rating: 800

n = int(input())

mTot = 0
cTot = 0

for _ in range(n):
    m, c = map(int, input().split())

    if m > c:
        mTot += 1

    if c > m:
        cTot += 1

if mTot > cTot:
    print("Mishka")
elif mTot < cTot:
    print("Chris")
else:
    print("Friendship is magic!^^")