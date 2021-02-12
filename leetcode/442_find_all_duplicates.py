class Solution:
    def findDuplicates(self, nums):
        res = []
        for n in nums:
            idx = abs(n) - 1
            if nums[idx] < 0:
                res.append(abs(n))
            else:
                nums[idx] = -nums[idx]
        return res


"""
Success
Details 
Runtime: 352 ms, faster than 78.23% of Python3 online submissions for Find All Duplicates in an Array.
Memory Usage: 21.9 MB, less than 41.74% of Python3 online submissions for Find All Duplicates in an Array.
Next challenges:
Find All Numbers Disappeared in an Array
"""
