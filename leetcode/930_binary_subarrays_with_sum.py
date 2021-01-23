
from typing import Dict


class Solution:
    def numSubarraysWithSum(self, A, S: int) -> int:
        counts: Dict[int, int] = {}
        pref_sums = [0]
        res = 0
        for n in A:
            pref_sums.append(pref_sums[-1]+n)
        for p in pref_sums:
            res += counts.get(p, 0)
            counts[p+S] = counts.get(p+S, 0) + 1
        return res


"""
Success
Details
Runtime: 276 ms, faster than 53.36% of Python3 online submissions for Binary
Subarrays With Sum.
Memory Usage: 18.8 MB, less than 7.65% of Python3 online submissions
for Binary Subarrays With Sum.
Next challenges:
Trapping Rain Water
Keyboard Row
Maximum Number of Visible Points
"""
