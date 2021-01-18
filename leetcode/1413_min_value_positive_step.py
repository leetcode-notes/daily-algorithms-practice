class Solution:
    def minStartValue(self, nums) -> int:
        running_min = nums[0]
        cur = nums[0]
        for i in range(1, len(nums)):
            cur += nums[i]
            running_min = min(running_min, cur)
        if running_min > 0:
            return 1
        return abs(running_min)+1


"""
Success
Details 
Runtime: 52 ms, faster than 10.79% of Python3 online submissions for Minimum Value to Get Positive Step by Step Sum.
Memory Usage: 14.2 MB, less than 43.85% of Python3 online submissions for Minimum Value to Get Positive Step by Step Sum.
Next challenges:
Find Minimum in Rotated Sorted Array II
Subarray Sums Divisible by K
Find the Minimum Number of Fibonacci Numbers Whose Sum Is K
Show off your acceptance:
"""
