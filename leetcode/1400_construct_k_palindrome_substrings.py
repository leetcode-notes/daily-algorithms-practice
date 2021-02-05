from collections import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        counts = Counter(s)
        odd_count = 0
        for v in counts.values():
            if v % 2:
                odd_count += 1
        if odd_count > k:
            return False
        return True


"""
Success
Details 
Runtime: 52 ms, faster than 99.84% of Python3 online submissions for Construct K Palindrome Strings.
Memory Usage: 14.8 MB, less than 93.84% of Python3 online submissions for Construct K Palindrome Strings.
Next challenges:
Queue Reconstruction by Height
Split Two Strings to Make Palindrome
Minimum Moves to Make Array Complementary
"""
