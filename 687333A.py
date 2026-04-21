# A. Axolotl
# https://codeforces.com/group/EW9LgKVDr6/contest/687333/problem/A

s = input()

axolotl = "axolotl"

toPrint = 0
for i in range(7):
    if s[i] == axolotl[i]:
        toPrint += 1

print(toPrint)