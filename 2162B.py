# B. Beautiful String
# https://codeforces.com/problemset/problem/2162/B
# rating: 1000

t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    toPrint = []
    for i in range(n):
        if s[i] == "0":
            toPrint.append(i + 1)
    
    print(s.count("0"))
    print(*toPrint)