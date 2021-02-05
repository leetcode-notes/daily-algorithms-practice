class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)
        for center in range(2*n-1):
            left = center // 2
            right = (center+1)//2
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
        return count


"""
Success
Details 
Runtime: 128 ms, faster than 80.20% of Python3 online submissions for Palindromic Substrings.
Memory Usage: 14 MB, less than 99.68% of Python3 online submissions for Palindromic Substrings.
Next challenges:
Wildcard Matching
Where Will the Ball Fall
Maximum Students Taking Exam
"""
