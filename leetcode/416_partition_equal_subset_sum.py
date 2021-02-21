class Solution:
    def canPartition(self, nums) -> bool:
        target = sum(nums)
        if target % 2:
            return False
        target //= 2
        dp = [[False]*(len(nums)) for _ in range(target+1)]
        for i in range(len(nums)):
            dp[0][i] = True

        for i in range(1, target+1):
            dp[i][0] = False

        for i in range(1, target+1):
            for j in range(1, len(nums)):
                dp[i][j] = dp[i][j-1]
                if i - nums[j-1] >= 0:
                    dp[i][j] = dp[i][j] or dp[i-nums[j-1]][j-1]

        return dp[target][len(nums)-1]


"""
Success
Details 
Runtime: 3764 ms, faster than 13.79% of Python3 online submissions for Partition Equal Subset Sum.
Memory Usage: 30.5 MB, less than 30.84% of Python3 online submissions for Partition Equal Subset Sum.
Next challenges:
Partition to K Equal Sum Subsets
"""
