import heapq
from collections import Counter


class Solution:
    def leastInterval(self, tasks, n: int) -> int:
        task_count = Counter(tasks)

        heap = []
        for task, count in task_count.items():
            heapq.heappush(heap, (-count, task))

        res = 0
        while heap:
            i, temp = 0, []
            while i <= n:
                res += 1
                if heap:
                    count, task = heapq.heappop(heap)
                    if count != -1:
                        temp.append((count+1, task))
                if not heap and not temp:
                    break
                else:
                    i += 1
            for item in temp:
                heapq.heappush(heap, item)
        return res


"""
Success
Details 
Runtime: 688 ms, faster than 16.38% of Python3 online submissions for Task Scheduler.
Memory Usage: 14.8 MB, less than 50.29% of Python3 online submissions for Task Scheduler.
Next challenges:
Rearrange String k Distance Apart
Show off your acceptance:
"""
