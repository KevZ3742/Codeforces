# B. Colourblindness
# https://codeforces.com/problemset/problem/1722/B
# rating: 800

t = int(input())

for _ in range(t):
    n = int(input())
    str1 = list(input())
    str2 = list(input())

    for i in range(n):
        if str1[i] == "G" or str1[i] == "B":
            str1[i] = "X"

        if str2[i] == "G" or str2[i] == "B":
            str2[i] = "X"

    if str1 == str2:
        print("YES")
    else:
        print("NO")