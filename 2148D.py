# D. Destruction of the Dandelion Fields
# https://codeforces.com/problemset/problem/2148/D
# rating: 1000

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()

    odd = []
    even = []
    for num in a:
        if num % 2:
            odd.append(num)
        else:
            even.append(num)

    if not odd:
        print(0)
        continue

    toPrint = odd[-1]

    for num in even:
        toPrint += num

    toPrint += sum(odd[(len(odd) // 2):len(odd) - 1]) 
    print(toPrint)