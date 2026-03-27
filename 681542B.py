# B. Card Trick
# https://codeforces.com/gym/681542/problem/B

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))

    bSum = sum(b)
    r = bSum % n

    print(a[r])