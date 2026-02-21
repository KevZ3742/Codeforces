# A. Anton and Letters
# https://codeforces.com/contest/443/problem/A
# rating: 800

letters = str(input())
letters = letters[1:-1]
letters = set(map(str.strip, letters.split(',')))

if letters == {''}:
    print(0)
else:
    print(len(letters))