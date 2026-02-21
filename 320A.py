# A. Magic Numbers
# https://codeforces.com/contest/320/problem/A
# rating: 900

n = str(input())

toPrint = "YES"
count4 = 0

for digit in n:
    if digit == "4":
        count4 += 1

        if count4 == 3:
            toPrint = "NO"
            break
    elif digit == "1":
        count4 = 0
    else:
        toPrint = "NO"
        break
    
if n[0] != "1":
    toPrint = "NO"

print(toPrint)