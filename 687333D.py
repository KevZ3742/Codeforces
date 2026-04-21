# D. Deciphering Seeds
# https://codeforces.com/group/EW9LgKVDr6/contest/687333/problem/D

from math import gcd

a, b = map(int, input().split())

divisors = [[] for _ in range(163)]
for s in range(1, 163):
    for divisor in range(2, s + 1):
        if s % divisor == 0:
            divisors[s].append(divisor)

def countValidSeeds(limit, digitSum):
    if limit == 0:
        return 0
    
    digits = list(map(int, str(limit)))
    digitCount = len(digits)
    
    divs = divisors[digitSum]
    if not divs:
        return 0
    
    memo = {}
    
    def dp(digitPos, curDigitSum, bound, mods):
        if digitPos == digitCount:
            if curDigitSum != digitSum:
                return 0
            
            for i in range(len(divs)):
                if mods[i] == 0:
                    return 1
            return 0
        
        key = (digitPos, curDigitSum, bound, mods)
        if key in memo:
            return memo[key]
        
        limitDigit = digits[digitPos] if bound else 9
        toReturn = 0
        
        for digit in range(limitDigit + 1):
            if curDigitSum + digit > digitSum:
                continue
            
            newMods = tuple((mods[i] * 10 + digit) % divs[i] for i in range(len(divs)))
            
            toReturn += dp(digitPos + 1, curDigitSum + digit, bound and (digit == limitDigit), newMods)
        
        memo[key] = toReturn
        return toReturn
    
    return dp(0, 0, True, tuple(0 for _ in divs))

def findSeeds(limit):
    if limit == 0:
        return 0
    
    total = 0
    maxDigitSum = min(162, len(str(limit)) * 9)
    
    for s in range(1, maxDigitSum + 1):
        total += countValidSeeds(limit, s)
    
    return total

print(findSeeds(b) - findSeeds(a - 1))

# tle