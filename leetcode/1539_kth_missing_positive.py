class Solution:
    def findKthPositive(self, arr, k) -> int:

        start = 1
        idx = 0
        missing = 0
        while idx < len(arr):
            if arr[idx] == start:
                idx += 1
            else:
                missing += 1
                if missing == k:
                    return start
            start += 1
        if missing < k:
            curr = arr[-1]
            while missing < k:
                curr += 1
                missing += 1
            return curr


"""
Success
Details
Runtime: 52 ms, faster than 62.52% of Python3
online submissions for Kth Missing Positive Number.
Memory Usage: 14.4 MB, less than 57.85% of
Python3 online submissions for Kth Missing Positive Number.
Next challenges:
Isomorphic Strings
Number of Boomerangs
Smallest Range Covering Elements from K Lists
"""
