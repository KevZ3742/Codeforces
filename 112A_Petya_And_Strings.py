# https://codeforces.com/problemset/problem/112/A
# rating: 800

str1 = str(input()).lower()
str2 = str(input()).lower()

if str1 == str2:
    print(0)
else:
    for i in range(len(str1)):
        if str1[i] > str2[i]:
            print(1)
            break
        elif str2[i] > str1[i]:
            print(-1)
            break

