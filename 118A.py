# A. String Task
# https://codeforces.com/contest/118/problem/A
# rating: 1000

string = str(input())

string = string.lower()

vowels = "aeiouy"
for char in vowels:
    if char in string:
        string = string.replace(char, "")

string = list(string)

print('.' + '.'.join(string))