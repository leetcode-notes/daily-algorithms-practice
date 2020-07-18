class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0]*(len(text2)+1) for _ in range(len(text1)+1)]

        m, n = len(text1), len(text2)
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]


'''
Success
Details
Runtime: 436 ms, faster than 75.74% of Python3
Memory Usage: 21.3 MB, less than 86.28% of Python3
Next challenges:
Delete Operation for Two Strings
Shortest Common Supersequence

Other DP+String combiantion problems (non premium)
with similar pattern or involving LCS as intermediate step

edit distance - https://leetcode.com/problems/edit-distance/
regex matching - https://leetcode.com/problems/regular-expression-matching/
wildcard matching - https://leetcode.com/problems/wildcard-matching/
shortest common supersequence (solution involves a LCS step)
 - https://leetcode.com/problems/shortest-common-supersequence
Longest Palindrome Subsequence (could be solved using LCS)
- https://leetcode.com/problems/longest-palindromic-subsequence/

If someone is finding hard to understand logic,
just be patient and go through
 https://www.cs.umd.edu/users/meesh/cmsc351/mount/lectures/lect25-longest-common-subseq.pdf.
 Believe me you'll never forget this concept ever.
'''
