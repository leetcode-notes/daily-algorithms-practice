class NumArray:

    def __init__(self, nums):
        if not nums:
            return
        self.nums = nums
        self.pref_sum = [0 for _ in range(len(nums))]
        self.pref_sum[0] = nums[0]
        for i in range(1, len(nums)):
            self.pref_sum[i] = self.pref_sum[i-1] + nums[i]

    def sumRange(self, i: int, j: int) -> int:
        if i == j:
            return self.nums[i]
        if i == 0:
            return self.pref_sum[j]
        else:
            return self.pref_sum[j] - self.pref_sum[i-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
'''
Success
Details
Runtime: 120 ms, faster than 45.60% of Python3
Memory Usage: 17.6 MB, less than 13.34% of Python3
Next challenges:
Range Sum Query 2D - Immutable
Range Sum Query - Mutable
Maximum Size Subarray Sum Equals k
'''
