class Solution:
    def sumZero(self, n: int):
        res = [0] * n
        for i in range(n):
            res[i] = i*2 - n + 1
        return res


'''
Success
Details
Runtime: 36 ms, faster than 44.08% of Python3
Memory Usage: 13.9 MB, less than 49.54% of Python3
Next challenges:
Maximal Rectangle
K-diff Pairs in an Array
Sort Array By Parity
'''
