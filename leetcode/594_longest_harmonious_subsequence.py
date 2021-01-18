class Solution:
    def findLHS(self, nums) -> int:
        count, res = {}, 0
        for n in nums:
            count[n] = count.get(n, 0)+1
        for n in count:
            if n+1 in count:
                res = max(res, count[n]+count[n+1])
        return res


"""
Success
Details
Runtime: 308 ms, faster than 56.08% of Python3
online submissions for Longest Harmonious Subsequence.
Memory Usage: 16 MB, less than
30.42% of Python3 online submissions for Longest Harmonious Subsequence.
Next challenges:
Minimum Area Rectangle
Maximum Equal Frequency
Count Good Meals
"""
