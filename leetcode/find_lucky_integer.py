from collections import Counter
from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        c = Counter(arr)
        max_lucky = 0
        for num in arr:
            if c[num] == num:
                max_lucky = max(max_lucky, num)
        return max_lucky if max_lucky > 0 else -1


s = Solution()
s.findLucky([1, 2, 3, 4])
