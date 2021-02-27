class Solution:
    def maxUncrossedLines(self, A, B) -> int:
        dp = [[0]*(len(B)+1) for _ in range(len(A)+1)]
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] == B[j]:
                    dp[i+1][j+1] = 1 + dp[i][j]
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        return dp[-1][-1]


"""
Success
Details 
Runtime: 192 ms, faster than 87.93% of Python3 online submissions for Uncrossed Lines.
Memory Usage: 14.5 MB, less than 71.52% of Python3 online submissions for Uncrossed Lines.
Next challenges:
Edit Distance
"""
