# rating: 900

p = str(input())

outputs = ["H", "Q", "9"]

output = False
for char in p:
    if char in outputs:
        output = True
        print("YES")
        break

if output == False:
    print("NO")