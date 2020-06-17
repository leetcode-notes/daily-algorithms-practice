class Solution:
    def intToRoman(self, num: int) -> str:
        thous, hundreds, tens, ones = 0, 0, 0, 0
        thous = num // 1000
        hundreds = num // 100 % 10
        tens = num // 10 % 10
        ones = num % 10
        res = []
        if thous > 0:
            while thous > 0:
                res.append("M")
                thous -= 1
        if hundreds == 9:
            res.append("CM")
            hundreds -= 9
        if hundreds >= 5:
            res.append("D")
            hundreds -= 5
        if hundreds == 4:
            res.append("CD")
            hundreds -= 4
        for _ in range(hundreds):
            res.append("C")
        if tens == 9:
            res.append("XC")
            tens -= 9
        if tens >= 5:
            res.append("L")
            tens -= 5
        if tens == 4:
            res.append("XL")
            tens -= 4
        for _ in range(tens):
            res.append("X")
        if ones == 9:
            res.append("IX")
            ones -= 9
        if ones >= 5:
            res.append("V")
            ones -= 5
        if ones == 4:
            res.append("IV")
            ones -= 4
        for _ in range(ones):
            res.append("I")
        return "".join(res)


'''
Success
Details
Runtime: 48 ms, faster than 74.51% of Python3...
Memory Usage: 13.8 MB, less than 61.77% of Python3...
Next challenges:
Roman to Integer
Integer to English Words
'''
