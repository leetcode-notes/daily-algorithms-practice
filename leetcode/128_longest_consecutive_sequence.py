import heapq


class Solution:
    def longestConsecutive(self, nums) -> int:
        heap, ans, temp = [], 1, 1
        for n in nums:
            heapq.heappush(heap, n)
        if not heap:
            return 0
        top = heapq.heappop(heap)
        while len(heap) > 0:
            cur = heapq.heappop(heap)
            if cur == top:
                continue
            elif cur == top+1:
                temp += 1
            else:
                temp = 1
            top = cur
            ans = max(ans, temp)
        return ans


"""
Success
Details
Runtime: 60 ms, faster than 34.59% of Python3 online
submissions for Longest Consecutive Sequence.
Memory Usage: 15.2 MB, less than 70.69% of Python3 online submissions
for Longest Consecutive Sequence.
Next challenges:
Binary Tree Longest Consecutive Sequence
"""
