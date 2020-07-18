class Solution(object):
    def maxProduct(self, nums):
        max_prod, min_prod, ans = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            temp_max_prod = max(nums[i], max_prod*nums[i], min_prod*nums[i])
            temp_min_prod = min(nums[i], max_prod*nums[i], min_prod*nums[i])
            max_prod = temp_max_prod
            min_prod = temp_min_prod
            ans = max(max_prod, ans)
        return ans


'''
Success
Details
Runtime: 60 ms, faster than 61.51% of Python3
Memory Usage: 14 MB, less than 65.36% of Python3
Next challenges:
Maximum Subarray
House Robber
Maximum Product of Three Numbers
Subarray Product Less Than K
'''
