from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(nums[i])
                continue
            res.append(res[i-1]+nums[i])
        return res


'''
Success
Details
Runtime: 36 ms, faster than 92.62% of Python3
Memory Usage: 14.1 MB, less than 33.33% of Python3y
Next challenges:
Insert Interval
Combination Sum III
Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
'''
