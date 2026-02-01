# rating: 800

s = str(input())

digits = [".", "-.", "--"]
number = ""

currDigit = ""
for i in s:
    currDigit += i

    for j in range(len(digits)):
        if digits[j] == currDigit:
            number += str(j)
            currDigit = ""

print(number)