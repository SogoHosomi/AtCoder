class Solution:
    def romanToInt(self, s: str) -> int:

        value = 0
        roman = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }

        for a, b in zip(s, s[1:]):
            if roman[a] < roman[b]:
                value -= roman[a]
            else:
                value += roman[a]
        
        return value + roman[s[-1]]
