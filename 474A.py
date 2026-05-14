# A. Keyboard
# https://codeforces.com/problemset/problem/474/A
# rating: 900

direction = input()
s = input()

l1 = "qwertyuiop"
l2 = "asdfghjkl;"
l3 = "zxcvbnm,./"

toPrint = ""

if direction == "R":
    for i in s:
        if i in l1:
            toPrint += l1[l1.index(i) - 1]
        elif i in l2:
            toPrint += l2[l2.index(i) - 1]
        elif i in l3:
            toPrint += l3[l3.index(i) - 1]
else:
    for i in s:
        if i in l1:
            toPrint += l1[l1.index(i) + 1]
        elif i in l2:
            toPrint += l2[l2.index(i) + 1]
        elif i in l3:
            toPrint += l3[l3.index(i) + 1]

print(toPrint)