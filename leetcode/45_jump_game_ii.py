class Solution:
    def jump(self, nums) -> int:

        steps = [2**32-1]*len(nums)
        steps[0] = 0
        n = len(nums)
        for i in range(len(nums)):
            for j in range(min(n-1, i+nums[i]), i, -1):
                if steps[j] > steps[i] + 1:
                    steps[j] = steps[i] + 1
                else:
                    break
        return steps[-1]


"""
Success
Details 
Runtime: 144 ms, faster than 32.23% of Python3 online submissions for Jump Game II.
Memory Usage: 16.4 MB, less than 11.79% of Python3 online submissions for Jump Game II.
Next challenges:
Jump Game III
"""
