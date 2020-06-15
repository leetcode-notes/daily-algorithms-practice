# keep track of number of "cracks" at each column
from typing import List


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        d = {}
        for row in wall:
            start = 0
            for i, v in enumerate(row):
                if i == len(row)-1:
                    continue
                start += v
                d[start] = 1 if start not in d else d[start]+1
        if not d:
            return len(wall)
        max_gaps = max(d.values())
        return len(wall) - max_gaps


test1 = [[1, 2, 2, 1],
         [3, 1, 2],
         [1, 3, 2],
         [2, 4],
         [3, 1, 2],
         [1, 3, 1, 1]]

s = Solution()
print(s.leastBricks(test1))


test2 = [[1], [1], [1]]

'''
Success
Details
Runtime: 200 ms, faster than 51.07% of Python3 online submissions...
Memory Usage: 19 MB, less than 5.60% of Python3 online submissions...
Next challenges:
Max Points on a Line
Rearrange String k Distance Apart
Daily Temperatures
'''
