from collections import Counter


class Solution:
    def subarraysWithKDistinct(self, A, K: int) -> int:

        def at_most_k(arr, k):
            count = Counter()
            left, res = 0, 0
            for right in range(len(arr)):
                if count[A[right]] == 0:
                    k -= 1
                count[A[right]] += 1
                while k < 0:
                    count[A[left]] -= 1
                    if count[A[left]] == 0:
                        k += 1
                    left += 1
                res += right - left + 1
            return res

        return at_most_k(A, K) - at_most_k(A, K-1)


"""
Success
Details 
Runtime: 816 ms, faster than 9.83% of Python3 online submissions for Subarrays with K Different Integers.
Memory Usage: 17.7 MB, less than 8.67% of Python3 online submissions for Subarrays with K Different Integers.
Next challenges:
Longest Substring with At Most Two Distinct Characters
Longest Substring with At Most K Distinct Characters
"""
