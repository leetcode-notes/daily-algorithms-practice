from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        first_half, second_half = nums[0:n], nums[n:]
        res = []
        for a, b in zip(first_half, second_half):
            res.append(a)
            res.append(b)
        return res
