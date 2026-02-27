# D. Divisibility Game
# https://codeforces.com/contest/2203/problem/D
# rating: ?

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    cap = n + m + 1

    alice = 0
    bob = 0
    both = 0

    a.sort()
    prev = -1
    aLenth = 0
    divisors = [0] * cap
    for num in a:
        if num == prev:
            continue
        prev = num
        aLenth += 1

        for multiple in range(num, cap, num):
            divisors[multiple] += 1

    for num in b:
        if divisors[num] == 0:
            bob += 1
        elif divisors[num] == aLenth:
            alice += 1
        else:
            both += 1

    alice += both % 2
 
    if alice > bob:
        print("Alice")
    else:
        print("Bob")