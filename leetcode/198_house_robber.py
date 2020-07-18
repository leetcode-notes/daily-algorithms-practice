class Solution:
    def rob(self, nums) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(nums[i]+dp[i-2], dp[i-1])
        return dp[-1]


'''
Success
Details
Runtime: 48 ms, faster than 19.07% of Python3
Memory Usage: 13.7 MB, less than 85.82% of Python3
Next challenges:
House Robber II
Paint House
Paint Fence
House Robber III
Non-negative Integers without Consecutive Ones
Coin Path
Delete and Earn
'''
