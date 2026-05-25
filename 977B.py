# B. Two-gram
# https://codeforces.com/problemset/problem/977/B
# rating: 900

def countFreq(pat, txt):
    M = len(pat)
    N = len(txt)
    res = 0

    for i in range(N - M + 1):
        j = 0
        while j < M:
            if (txt[i + j] != pat[j]):
                break
            j += 1

        if (j == M):
            res += 1
            j = 0
    return res

n = int(input())
s = input()

occurances = 0
toPrint = ""
for i in range(1, n):
    freq = countFreq(s[i - 1:i + 1], s)

    temp = occurances
    occurances = max(occurances, freq)

    if occurances != temp:
        toPrint = s[i - 1:i + 1]

print(toPrint)