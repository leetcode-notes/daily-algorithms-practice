import heapq
from collections import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        res = ""
        heap = []
        counts = Counter(s)
        for k, v in counts.items():
            heapq.heappush(heap, (-v, k))
        temp = []
        while len(heap) > 1:
            count, ch = heapq.heappop(heap)
            count2, ch2 = heapq.heappop(heap)

            res += ch
            res += ch2
            if count < -1:
                heapq.heappush(heap, (count+1, ch))
            if count2 < -1:
                heapq.heappush(heap, (count2+1, ch2))
        if heap:
            count, ch = heap[0]
            if count < -1:
                return ""
            else:
                res += ch
        return res


"""
Success
Details 
Runtime: 28 ms, faster than 92.45% of Python3 online submissions for Reorganize String.
Memory Usage: 14.2 MB, less than 84.12% of Python3 online submissions for Reorganize String.
Next challenges:
Rearrange String k Distance Apart
Show off your acceptance:
Time Submitted
Status
Runtime
Memory
Language
07/11/2021 21:06	Accepted	28 ms	14.2 MB	python3
"""
