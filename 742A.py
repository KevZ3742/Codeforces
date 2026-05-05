# A. Arpa’s hard exam and Mehrdad’s naive cheat
# https://codeforces.com/problemset/problem/742/A
# rating: 1000

n = int(input())

if n == 0:
    print(1)
else:
    check = n % 4

    if check == 1:
        print(8)
    
    if check == 2:
        print(4)

    if check == 3:
        print(2)

    if check == 0:
        print(6)