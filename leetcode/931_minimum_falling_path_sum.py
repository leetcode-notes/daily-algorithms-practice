class Solution:
    """
    matrix   dp
    2 1 3    2 1 3
    6 5 4    7 6 5
    7 8 9   13 13  13
    """

    def minFallingPathSum(self, matrix) -> int:

        dp = [[0]*len(matrix[0]) for _ in range(len(matrix))]
        for i, n in enumerate(matrix[0]):
            dp[0][i] = n
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                if j == 0:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j+1]) + matrix[i][j]
                elif j == len(matrix[0])-1:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + matrix[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j],
                                   dp[i-1][j+1]) + matrix[i][j]

        return min(dp[-1])


"""
Success
Details 
Runtime: 112 ms, faster than 86.90% of Python3 online submissions for Minimum Falling Path Sum.
Memory Usage: 15.3 MB, less than 34.33% of Python3 online submissions for Minimum Falling Path Sum.
Next challenges:
Minimum Falling Path Sum II
"""
