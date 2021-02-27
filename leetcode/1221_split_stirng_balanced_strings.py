class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r, l = 0, 0
        count = 0
        for ch in s:

            if ch == "R":
                r += 1
            elif ch == "L":
                l += 1
            if l == r and l != 0:
                count += 1
                r = 0
                l = 0
        return count


"""
Success
Details 
Runtime: 28 ms, faster than 85.36% of Python3 online submissions for Split a String in Balanced Strings.
Memory Usage: 14.3 MB, less than 13.70% of Python3 online submissions for Split a String in Balanced Strings.
Next challenges:
Number of Segments in a String
Smallest Subsequence of Distinct Characters
Stone Game VI
"""
