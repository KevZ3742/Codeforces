# C. Test Generator
# https://codeforces.com/contest/2203/problem/C
# rating: ?

t = int(input())

for _ in range(t):
    s, m = map(int, input().split())

    a = m & -m
    if s % a != 0:
        print(-1)
        continue

    bits = []
    temp = m
    while temp:
        lowest = temp & -temp
        bits.append((lowest))
        temp -= lowest

    bits.sort(reverse=True)

    l, r = 0, s
    while l < r:
        mid = (l + r) // 2
        tempS = s

        for bit in bits:
            tempS -= min(mid, tempS // bit) * bit
            if tempS == 0:
                break
        
        if tempS == 0:
            r = mid
        else:
            l = mid + 1

    print(l)