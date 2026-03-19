# B. Shifts and Sorting
# https://codeforces.com/problemset/problem/1969/B
# rating: 1000

t = int(input())

for _ in range(t):
    s = input()

    if s.count("1") == 0 or s.count("0") == 0:
        print(0)
        continue

    toPrint = 0
    inPlace = 0
    length = 0

    first = True

    for char in s:
        if char == "1":
            length += 1
            first = False
        else:
            if first:
                continue
            
            length += 1
            toPrint += length - inPlace
            inPlace += 1

    print(toPrint)
        