class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        seen = {}
        left, max_len = 0, 0
        for right in range(len(s)):
            seen[s[right]] = 1 if s[right] not in seen else seen[s[right]] + 1
            while len(seen) > 2:
                seen[s[left]] -= 1
                if seen[s[left]] == 0:
                    del seen[s[left]]
                left += 1
            max_len = max(max_len, right-left+1)
        return max_len


"""
Success
Details 
Runtime: 60 ms, faster than 54.68% of Python3 online submissions for Longest Substring with At Most Two Distinct Characters.
Memory Usage: 14.5 MB, less than 47.25% of Python3 online submissions for Longest Substring with At Most Two Distinct Characters.
Next challenges:
Sliding Window Maximum
"""
