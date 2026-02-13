# rating: 1100

file = open("input.txt", "r")
output = open("output.txt", "w")

n, m = map(int, file.readline().split())

repeatCount = min(n, m)
remainder = max(n, m) - repeatCount

if n > m:
    toRepeat = "BG"
    toIterate = "B"
else:
    toRepeat = "GB"
    toIterate = "G"

output.write(toRepeat * repeatCount + toIterate * remainder)