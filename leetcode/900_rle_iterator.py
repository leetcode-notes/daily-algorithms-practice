class RLEIterator:

    def __init__(self, A: List[int]):
        self.sequence = A
        self.index = 0

    def next(self, n: int) -> int:
        if self.index >= len(self.sequence):
            return -1
        count = self.sequence[self.index]
        val = self.sequence[self.index+1]
        if count >= n:
            count -= n
            self.sequence[self.index] = count
            return val
        else:
            n -= count
            while n:
                self.index += 2
                if self.index >= len(self.sequence):
                    return -1
                count = self.sequence[self.index]
                val = self.sequence[self.index+1]
                if count >= n:
                    count -= n
                    self.sequence[self.index] = count
                    return val
                else:
                    n -= count


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)
"""
Success
Details
Runtime: 40 ms, faster than 62.43 % of Python3 online submissions for RLE Iterator.
Memory Usage: 14.8 MB, less than 64.19 % of Python3 online submissions for RLE Iterator.
Next challenges:
3Sum Smaller
Maximum Swap
High Five
"""
