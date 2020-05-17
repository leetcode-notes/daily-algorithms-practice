from typing import List


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count: int = 0
        for start, end in zip(startTime, endTime):
            if queryTime >= start and queryTime <= end:
                count += 1
        return count
