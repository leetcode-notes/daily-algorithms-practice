class Solution:
    def sortArrayByParityII(self, A):
        odds, evens = [], []
        for n in A:
            if n % 2:
                odds.append(n)
            else:
                evens.append(n)
        res = []
        for i in range(len(A)):
            if i % 2:
                res.append(odds[-1])
                odds.pop()
            else:
                res.append(evens[-1])
                evens.pop()
        return res


"""
Success
Details
Runtime: 220 ms, faster than 30.41% of Python3
 online submissions for Sort Array By Parity II.
Memory Usage: 16.6 MB, less than 62.65% of Python3
online submissions for Sort Array By Parity II.
Next challenges:
Game of Life
Count Triplets That Can Form Two Arrays of Equal XOR
Avoid Flood in The City
"""
