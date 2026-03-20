# B. Flipping Binary String
# https://codeforces.com/problemset/problem/2192/B
# rating: 1000

t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    ones = s.count("1")
    zeros = s.count("0")
    toPrint = []

    if ones % 2:
        if len(s) % 2:
            print(-1)
        else:
            print(zeros)
        
            for i in range(n):
                if s[i] == "0":
                    toPrint.append(i + 1)

            print(*toPrint)
    else:
        print(ones)

        if ones == 0:
            continue
        
        for i in range(n):
            if s[i] == "1":
                toPrint.append(i + 1)

        print(*toPrint)