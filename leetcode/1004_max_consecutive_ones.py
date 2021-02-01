class Solution:
    def longestOnes(self, A, K: int) -> int:
        left, right = 0, 0

        for right in range(len(A)):
            if A[right] == 0:
                K -= 1
            if K < 0:
                if A[left] == 0:
                    K += 1
                left += 1
        return right - left + 1


"""
Success
Details 
Runtime: 540 ms, faster than 98.95% of Python3 online submissions for Max Consecutive Ones III.
Memory Usage: 14.7 MB, less than 91.39% of Python3 online submissions for Max Consecutive Ones III.
Next challenges:
Longest Substring with At Most K Distinct Characters
Longest Repeating Character Replacement
Max Consecutive Ones II
Show off your acceptance:
"""
