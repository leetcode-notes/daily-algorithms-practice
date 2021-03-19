from collections import Counter


class Solution:
    def numSplits(self, s: str) -> int:
        left_unique, right_unique = Counter(), Counter(s)
        count = 0
        for ch in s:
            left_unique[ch] += 1
            right_unique[ch] -= 1
            if right_unique[ch] == 0:
                del right_unique[ch]
            if len(left_unique) == len(right_unique):
                count += 1
        return count


"""
Success
Details
Runtime: 228 ms, faster than 41.86 % of Python3 online submissions for Number of Good Ways to Split a String.
Memory Usage: 14.9 MB, less than 40.82 % of Python3 online submissions for Number of Good Ways to Split a String.
Next challenges:
Complex Number Multiplication
Split Array into Fibonacci Sequence
Number of Distinct Substrings in a String
"""
