from collections import defaultdict, deque


class Solution:
    def canReach(self, arr, start: int) -> bool:
        graph = defaultdict(list)
        for i, n in enumerate(arr):
            next_pos = n + i
            if next_pos < len(arr):
                graph[i].append(next_pos)
            if i - n >= 0:
                prev_pos = i - n
                graph[i].append(prev_pos)

        seen = set()
        queue = deque([])
        queue.append(start)
        seen.add(start)
        while queue:
            cur = queue.popleft()
            if arr[cur] == 0:
                return True
            for nei in graph[cur]:
                if nei not in seen:
                    queue.append(nei)
                    seen.add(nei)
        return False


"""
Success
Details 
Runtime: 376 ms, faster than 13.77% of Python3 online submissions for Jump Game III.
Memory Usage: 31.6 MB, less than 46.33% of Python3 online submissions for Jump Game III.
Next challenges:
Clone Graph
Binary Tree Tilt
Maximum Product of Splitted Binary Tree
"""
