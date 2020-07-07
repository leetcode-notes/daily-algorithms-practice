class Solution:
    def maxDistToClosest(self, seats) -> int:
        prev, dist = None, 0
        for i, n in enumerate(seats):
            if n == 1:
                if prev is None:
                    dist = i
                else:
                    dist = max(dist, (i - prev)//2)
                prev = i
        return max(dist, len(seats)-1-prev)


'''
Success
Details
Runtime: 168 ms, faster than 33.13% of Python3
Memory Usage: 14.3 MB, less than 57.01% of Python3
Next challenges:
Exam Room
'''
