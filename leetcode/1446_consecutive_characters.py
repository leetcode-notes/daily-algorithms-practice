class Solution:
    def maxPower(self, s: str) -> int:
        length, max_length = 1, 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                length += 1
            else:
                length = 1
            max_length = max(max_length, length)
        return max_length
