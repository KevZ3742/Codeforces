# https://codeforces.com/problemset/problem/118/A
# rating: 1000

string = str(input())

string = string.lower()

vowels = "aeiouy"
for char in vowels:
    if char in string:
        string = string.replace(char, "")

string = list(string)

counter = 0
for i in range(len(string)):
    string.insert(i+counter, ".")
    counter += 1

print(''.join(string))