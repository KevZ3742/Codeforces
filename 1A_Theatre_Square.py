# https://codeforces.com/problemset/problem/1/A

import math

input = input()
inputs = input.split()

x = math.ceil(int(inputs[0]) / int(inputs[2]))
y = math.ceil(int(inputs[1]) / int(inputs[2]))

print(x * y)