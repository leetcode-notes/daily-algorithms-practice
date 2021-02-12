class Solution:
    def findDisappearedNumbers(self, nums):
        res = []
        for n in nums:
            idx = abs(n)-1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i+1)
        return res


"""
Success
Details 
Runtime: 356 ms, faster than 64.72% of Python3 online submissions for Find All Numbers Disappeared in an Array.
Memory Usage: 21.8 MB, less than 81.25% of Python3 online submissions for Find All Numbers Disappeared in an Array.
Next challenges:
First Missing Positive
"""
