class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hits = [[0, i+1] for i in range(300)]

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        index = (timestamp % 300) - 1
        freq, prev_time = self.hits[index][0], self.hits[index][1]
        if timestamp == prev_time:
            self.hits[index] = [freq+1, timestamp]
        else:
            self.hits[index] = [1, timestamp]

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        count = 0
        for freq, time in self.hits:
            if timestamp-time < 300:
                count += freq
        return count


# [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5)]
# hit(6)
# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(1)
# obj.hit(4)
# obj.hit(300)
# obj.hit(301)
# print(obj.getHits(301))

"""
Success
Details 
Runtime: 32 ms, faster than 65.10% of Python3 online submissions for Design Hit Counter.
Memory Usage: 14.6 MB, less than 20.86% of Python3 online submissions for Design Hit Counter.
Next challenges:
Logger Rate Limiter
Show off your acceptance:
"""
