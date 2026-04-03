# B. AccurateLee
# https://codeforces.com/gym/683153/problem/B

t = int(input())
 
for _ in range(t):
    n = int(input())
    s = input()

    if s.count(s[0]) == n:
        print(s)
        continue

    if "10" not in s:
        print(s)
        continue

    toPrint = []

    i = 0
    while i < n and s[i] == "0":
        toPrint.append("0")
        i += 1

    toPrint.append("0")

    i = n - 1
    while i >= 0 and s[i] == "1":
        toPrint.append("1")
        i -= 1

    print("".join(toPrint))