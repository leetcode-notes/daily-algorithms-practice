from collections import defaultdict
from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        d = defaultdict(list)
        modSixty = []
        maxTime = 960
        count = 0
        while maxTime > 0:
            if maxTime % 60 == 0:
                modSixty.append(maxTime)
            maxTime -= 60
        for i, t1 in enumerate(time):
            d[t1].append(i)
            for t2 in modSixty:
                target = t2-t1
                if target < 0:
                    continue
                if target in d:
                    for j in d[target]:
                        if j < i:
                            count += 1
        return count


'''
Success
Details
Runtime: 3208 ms, faster than 5.05% of Python3
Memory Usage: 17.2 MB, less than 25.95% of Python3
Next challenges:
Moving Stones Until Consecutive II
Remove Sub-Folders from the Filesystem
Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
'''
