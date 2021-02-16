import heapq


class KthLargest:

    def __init__(self, k: int, nums):
        self.heap = []
        self.k = k
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


"""
Success
Details 
Runtime: 92 ms, faster than 89.99% of Python3 online submissions for Kth Largest Element in a Stream.
Memory Usage: 18.5 MB, less than 17.69% of Python3 online submissions for Kth Largest Element in a Stream.
Next challenges:
Design Snake Game
All O`one Data Structure
Design Skiplist
"""
