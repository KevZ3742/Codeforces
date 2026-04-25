# A. Ilya and Bank Account
# https://codeforces.com/problemset/problem/313/A
# rating: 900

n = int(input())
 
if n >= 0:
    print(n)
else:
    s = str(n)
    option1 = int(s[:-1])
    option2 = int(s[:-2] + s[-1])
    
    print(max(option1, option2))