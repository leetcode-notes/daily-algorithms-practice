class Solution:
    def minEatingSpeed(self, piles, H: int) -> int:
        low, high = 1, max(piles)

        def cannot_finish(k, piles):
            total = 0
            for p in piles:
                total += p//k
                if p % k:
                    total += 1
            return total > H

        while low < high:
            mid = low + (high-low)//2
            if cannot_finish(mid, piles):
                low = mid + 1
            else:
                high = mid
        return low


"""
Success
Details
Runtime: 500 ms, faster than 53.72% of Python3 online
 submissions for Koko Eating Bananas.
Memory Usage: 15.4 MB, less than 76.05% of Python3 online
 submissions for Koko Eating Bananas.
Next challenges:
Minimize Max Distance to Gas Station
"""
