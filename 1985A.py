# A. Creating Words
# https://codeforces.com/problemset/problem/1985/A
# rating: 800

t = int(input())

for _ in range(t):
    str1, str2 = input().split()

    print(str2[0] + str1[1:], str1[0] + str2[1:])