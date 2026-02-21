# A. Little Elephant and Bits
# https://codeforces.com/contest/258/problem/A
# rating: 1100

a = list(input())
a0 = a.count("0")

if a0 == 0:
    a.pop()
    print("".join(a))
else:
    a[a.index("0")] = ""
    print("".join(a))