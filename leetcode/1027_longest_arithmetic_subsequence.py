from collections import defaultdict


class Solution:
    def longestArithSeqLength(self, A) -> int:
        dp = defaultdict(dict)
        for i in range(len(A)):
            for j in range(i):
                d = A[i] - A[j]
                dp[i][d] = 1 + dp[j].get(d, 1)
        res = 2
        for v in dp.values():
            for length in v.values():
                res = max(res, length)
        return res


'''
Success
Details
Runtime: 1272 ms, faster than 76.39 % of Python3
Memory Usage: 146.4 MB, less than 77.61 % of Python3
Next challenges:
Super Washing Machines
Find the Shortest Superstring
Binary Tree Cameras
'''
