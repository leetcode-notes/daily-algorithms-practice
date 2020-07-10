class Solution:
    def findLongestChain(self, pairs) -> int:
        pairs.sort()
        dp = [1 for _ in range(len(pairs))]
        for i in range(len(pairs)):
            for j in range(i):
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)


'''
Success
Details
Runtime: 4228 ms, faster than 6.86% of Python3
Memory Usage: 14.4 MB, less than 15.34% of Python3
Next challenges:
Increasing Subsequences
'''
