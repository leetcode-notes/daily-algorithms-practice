class LogSystem:

    def __init__(self):
        self.times = []
        self.granularity = {"Year": 4, "Month": 7,
                            "Day": 10, "Hour": 13, "Minute": 16, "Second": 19}

    def put(self, id: int, timestamp: str) -> None:
        self.times.append([timestamp, id])

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        index = self.granularity[granularity]
        start, end = start[:index], end[:index]
        result = []
        for time, tweet_id in self.times:
            if start <= time[:index] <= end:
                result.append(tweet_id)
        return result


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)

"""
Success
Details 
Runtime: 52 ms, faster than 74.07% of Python3 online submissions for Design Log Storage System.
Memory Usage: 14.5 MB, less than 84.49% of Python3 online submissions for Design Log Storage System.
Next challenges:
Design In-Memory File System
"""
