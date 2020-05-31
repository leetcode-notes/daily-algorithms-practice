from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_elem = max(nums)
        idx = nums.index(max_elem)
        max_elem -= 1
        max_prod = 0
        for i in range(len(nums)):
            if i == idx:
                continue
            else:
                cur = nums[i]-1
                max_prod = max(max_prod, max_elem*cur)
        return max_prod


nums = [3, 4, 5, 2]
s = Solution()
print(s.maxProduct(nums))
