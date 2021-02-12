class Solution:
    def checkArithmeticSubarrays(self, nums, l, r):

        def is_arithmetic(arr):
            arr.sort()
            diff = arr[1] - arr[0]
            for i in range(1, len(arr)):
                if arr[i] - arr[i-1] != diff:
                    return False
            return True
        res = []
        for i, j in zip(l, r):
            temp = nums[i:j+1]
            ans = is_arithmetic(temp)
            res.append(ans)
        return res


"""
Success
Details 
Runtime: 180 ms, faster than 94.82% of Python3 online submissions for Arithmetic Subarrays.
Memory Usage: 14.4 MB, less than 67.76% of Python3 online submissions for Arithmetic Subarrays.
Next challenges:
Sort Colors
Contains Duplicate III
Count of Range Sum
"""
