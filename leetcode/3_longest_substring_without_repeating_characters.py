class Solution:

    def lengthOfLongestSubstring(self, string):

        longest = 0
        left, right = 0, 0
        chars = set()
        while left < len(string) and right < len(string):
            if string[right] not in chars:
                chars.add(string[right])
                right += 1
                longest = max(longest, right - left)
            else:
                chars.remove(string[left])
                left += 1
        return longest


'''
Success
Details
Runtime: 124 ms, faster than 25.57% of Python3
Memory Usage: 13.9 MB, less than 62.02% of Python3
Next challenges:
Longest Substring with At Most Two Distinct Characters
Longest Substring with At Most K Distinct Characters
Subarrays with K Different Integers
'''
