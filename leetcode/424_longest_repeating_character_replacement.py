from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = Counter()
        left, max_len = 0, 0
        for right in range(len(s)):
            counts[s[right]] += 1
            while (right-left+1) - max(counts.values()) > k:
                counts[s[left]] -= 1
                left += 1
            max_len = max(max_len, right-left+1)
        return max_len


"""
Success
Details 
Runtime: 184 ms, faster than 32.26% of Python3 online submissions for Longest Repeating Character Replacement.
Memory Usage: 14.2 MB, less than 83.89% of Python3 online submissions for Longest Repeating Character Replacement.
Next challenges:
Sort Transformed Array
Circular Array Loop
Permutation in String
"""
