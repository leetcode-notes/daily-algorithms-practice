from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        seen = defaultdict(int)
        left, max_len = 0, 0
        for right in range(len(s)):
            seen[s[right]] += 1
            while len(seen) > k:
                seen[s[left]] -= 1
                if seen[s[left]] == 0:
                    del seen[s[left]]
                left += 1
            max_len = max(max_len, right-left+1)
        return max_len


"""
Success
Details 
Runtime: 80 ms, faster than 65.46% of Python3 online submissions for Longest Substring with At Most K Distinct Characters.
Memory Usage: 14.2 MB, less than 85.87% of Python3 online submissions for Longest Substring with At Most K Distinct Characters.
Next challenges:
Longest Repeating Character Replacement
"""
