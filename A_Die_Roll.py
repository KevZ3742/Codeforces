# rating: 800

import math

y, w = map(int, input().split())

numerator = (6 - max(y,w) + 1)
gcd = math.gcd(numerator, 6)

print(str(numerator // gcd) + "/" + str(6 // gcd))
