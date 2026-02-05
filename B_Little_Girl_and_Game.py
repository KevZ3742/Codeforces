# rating: 1300

from collections import Counter

s = Counter(input())

arr = []
for letter in s.keys():
    if s[letter] % 2 == 1:
        arr.append(letter)
        
if len(arr) == 0 or len(arr) == 1:
    print("First")
elif len(arr) % 2 == 0:
    print("Second")
else:
    print("First")