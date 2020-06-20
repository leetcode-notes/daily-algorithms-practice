from typing import List


class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        cur_max = A[0]
        ans = 0
        for i, n in enumerate(A):
            if i == 0:
                continue
            cur_max -= 1
            ans = max(ans, n+cur_max)
            cur_max = max(cur_max, n)
        return ans


'''
Success
Details
Runtime: 520 ms, faster than 57.14% of Python3
Memory Usage: 19.1 MB, less than 52.97% of Python3
Next challenges:
Find Peak Element
Length of Longest Fibonacci Subsequence
Online Majority Element In Subarray
'''
