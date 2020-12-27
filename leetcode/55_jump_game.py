class Solution:
    def canJump(self, nums):
        max_reach, n = 0, len(nums)
        for i in range(n):
            if max_reach < i:
                return False
            if max_reach >= (n-1):
                return True
            max_reach = max(max_reach, i+nums[i])


"""
Success
Details
Runtime: 84 ms, faster than 74.64% of
 Python3 online submissions for Jump Game.
Memory Usage: 16.2 MB, less than 12.48% of Python3
online submissions for Jump Game.
Next challenges:
Jump Game II
Jump Game III
"""
