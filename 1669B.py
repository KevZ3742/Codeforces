# B. Triple
# https://codeforces.com/problemset/problem/1669/B
# rating: 800

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    counter = [0] * (max(a) + 1)
    for num in a:
        counter[num] += 1

    for i in range(len(counter)):
        if counter[i] >= 3:
            print(i)
            break
    else:
        print(-1)