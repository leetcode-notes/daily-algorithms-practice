class Solution:
    def minPathSum(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, n):
            dp[0][i] = dp[0][i-1] + grid[0][i]

        for j in range(1, m):
            dp[j][0] = dp[j-1][0] + grid[j][0]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]


'''
Success
Details
Runtime: 128 ms, faster than 32.58% of Python3
Memory Usage: 15.3 MB, less than 54.95% of Python3
Next challenges:
Unique Paths
Dungeon Game
Cherry Pickup
'''
