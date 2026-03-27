# A. Game with Cards
# https://codeforces.com/gym/681542/problem/A

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))

    alice = max(a)
    bob = max(b)

    if alice >= bob:
        print("Alice")
    else:
        print("Bob")

    if bob >= alice:
        print("Bob")
    else:
        print("Alice")