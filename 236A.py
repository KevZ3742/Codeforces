# A. Boy or Girl
# https://codeforces.com/contest/236/problem/A
# rating: 800

uniqueChars = set(list(str(input())))

if len(uniqueChars) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")