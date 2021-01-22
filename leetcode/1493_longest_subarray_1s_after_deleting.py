class Solution:
    def longestSubarray(self, nums) -> int:
        # find all windows with  with at most 1 zero
        res, left = 0, 0
        ones = 0
        for i in range(len(nums)):
            ones += nums[i]
            while left < i and ones < i - left:
                ones -= nums[left]
                left += 1
            res = max(res, i-left)
        return res


"""
Success
Details 
Runtime: 428 ms, faster than 30.18% of Python3 online submissions
for Longest Subarray of 1's After Deleting One Element.
Memory Usage: 16.8 MB, less than 48.56% of Python3 online submissions
for Longest Subarray of 1's After Deleting One Element.
Next challenges:
Max Consecutive Ones
Valid Mountain Array
Queries on a Permutation With Key
"""
