class Solution:
    def longestPalindromeSubseq(self, s):
        if not s:
            return 0
        dp = [[0]*len(s) for _ in range(len(s))]
        for i in range(len(s)-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][-1]


'''
Success
Details
Runtime: 2644 ms, faster than 30.81% of Python3
Memory Usage: 30.3 MB, less than 70.61% of Python3
Next challenges:
Longest Palindromic Substring
Palindromic Substrings
Count Different Palindromic Subsequences
Longest Common Subsequence
'''
