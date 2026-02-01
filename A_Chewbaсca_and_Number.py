# rating: 1200

num = str(input())

toPrint = ""

for i in range(len(num)):
    if i == 0 and num[i] == "9":
        toPrint += "9"
    elif int(num[i]) < 9 - int(num[i]):
        toPrint += num[i]
    else:
        toPrint += str(9 - int(num[i]))

print(int(toPrint))