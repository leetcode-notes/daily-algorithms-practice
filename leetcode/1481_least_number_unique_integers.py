from collections import Counter


class Solution:
    def findLeastNumOfUniqueInts(self, arr, k: int) -> int:
        counts = Counter(arr)
        vals = sorted(list(counts.values()))
        count = 0
        while k > 0:
            for v in vals:
                if k >= v:
                    k -= v
                    count += 1
                else:
                    k -= v

        return len(counts)-count


'''
Success
Details
Runtime: 616 ms, faster than 69.32% of Python3Removals.
Memory Usage: 30.1 MB, less than 66.67% of Python3
Next challenges:
Jump Game
Can Place Flowers
Pancake Sorting
'''
