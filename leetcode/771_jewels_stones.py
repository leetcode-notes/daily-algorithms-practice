from collections import Counter


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        counts = Counter(J)
        jewels = 0
        for c in S:
            if c in counts:
                jewels += 1
        return jewels


'''
Success
Details
Runtime: 40 ms, faster than 21.61% of Python3
Memory Usage: 14 MB, less than 17.56% of Python3
Next challenges:
Design Twitter
Design HashMap
N-Repeated Element in Size 2N Array
'''
