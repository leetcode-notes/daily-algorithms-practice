class Solution:
    def longestSubsequence(self, arr, difference: int) -> int:
        d, res = {}, -2**32
        for n in arr:
            target = n - difference
            count = 1
            if target in d:
                count += d[target]
            d[n] = count
            res = max(res, d[n])
        return res


'''
Details
Runtime: 656 ms, faster than 51.00% of Python3
Memory Usage: 27.1 MB, less than 45.53% of Python3
Next challenges:
Super Ugly Number
Largest Triangle Area
Build Array Where You Can Find The Maximum Exactly K Comparisons
'''
