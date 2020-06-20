from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        cur = arr[0]
        count = 1
        if len(arr) == 1:
            return arr[0]
        for n in arr[1:]:
            if n == cur:
                count += 1
            else:
                cur = n
                count = 1
            if count/len(arr) > 0.25:
                return cur
        return -1


'''
Success
Details
Runtime: 92 ms, faster than 81.78 % of Python3...
Memory Usage: 14.8 MB, less than 99.41 % of Python3...
Next challenges:
Find Minimum in Rotated Sorted Array II
Pairs of Songs With Total Durations Divisible by 60
Moving Stones Until Consecutive II
'''
