import heapq


class Solution:
    def eatenApples(self, apples, days) -> int:
        """
        always eat the apple(s) with soonest expiration
        """
        heap = []
        eaten = 0
        for i in range(len(apples)):
            heapq.heappush(heap, [i+days[i], apples[i]])
            while heap:
                if heap[0][0] <= i or heap[0][1] < 1:
                    heapq.heappop(heap)
                else:
                    if heap[0][1] > 0:
                        eaten += 1
                        heap[0][1] -= 1
                        break

        cur_day = i + 1
        while heap:
            if heap[0][0] <= cur_day or heap[0][1] < 1:
                heapq.heappop(heap)
            else:
                if heap[0][1] > 0:
                    eaten += 1
                    heap[0][1] -= 1
                    cur_day += 1
        return eaten


"""
Success
Details 
Runtime: 660 ms, faster than 73.51% of Python3 online submissions for Maximum Number of Eaten Apples.
Memory Usage: 18.9 MB, less than 17.38% of Python3 online submissions for Maximum Number of Eaten Apples.
Next challenges:
Partition Labels
Split a String in Balanced Strings
Smallest String With A Given Numeric Value
"""
