from collections import deque


class Solution:
    def maxSlidingWindow(self, nums, k: int):
        mono = deque()
        res = []
        for i, n in enumerate(nums):

            if mono and i - mono[0] >= k:
                mono.popleft()

            while mono and nums[mono[-1]] < n:
                mono.pop()

            mono.append(i)
            if i >= k-1:
                res.append(nums[mono[0]])
        return res


"""
Success
Details 
Runtime: 1716 ms, faster than 38.97% of Python3 online submissions for Sliding Window Maximum.
Memory Usage: 30.2 MB, less than 26.37% of Python3 online submissions for Sliding Window Maximum.
Next challenges:
Minimum Window Substring
Min Stack
Paint House II
Jump Game VI
Show off your acceptance:
"""
