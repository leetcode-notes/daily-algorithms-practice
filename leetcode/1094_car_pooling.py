from collections import defaultdict


class Solution:
    def carPooling(self, trips, capacity: int) -> bool:
        points = set()
        pickup, dropoff = defaultdict(int), defaultdict(int)
        for p, s, e in trips:
            points.add(s)
            points.add(e)
            pickup[s] += p
            dropoff[e] += p
        points = sorted(list(points))
        cur = 0
        for p in points:
            if p in pickup:
                cur += pickup[p]
            if p in dropoff:
                cur -= dropoff[p]
            if cur > capacity:
                return False
        return True


'''
Success
Details
Runtime: 80 ms, faster than 44.16% of Python3
Memory Usage: 14.3 MB, less than 33.33% of Python3
Next challenges:
Meeting Rooms II
'''
