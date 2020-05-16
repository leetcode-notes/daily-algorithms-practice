from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        cur_max = max(candies)
        res = []
        for c in candies:
            if c+extraCandies >= cur_max:
                res.append(True)
            else:
                res.append(False)
        return res
