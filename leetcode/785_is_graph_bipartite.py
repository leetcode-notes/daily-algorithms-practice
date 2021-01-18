from collections import deque


class Solution:
    def isBipartite(self, graph) -> bool:
        visited = {}

        def bfs(start):
            queue = deque([(start, 1)])
            while queue:
                cur, color = queue.popleft()
                if cur in visited:
                    if visited[cur] != color:
                        return False
                    continue
                visited[cur] = color
                for nei in graph[cur]:
                    queue.append((nei, -color))
            return True

        for i in range(len(graph)):
            if i not in visited:
                if not bfs(i):
                    return False
        return True


"""
Success
Details 
Runtime: 288 ms, faster than 8.80% of Python3 online submissions for Is Graph Bipartite?.
Memory Usage: 14.8 MB, less than 33.77% of Python3 online submissions for Is Graph Bipartite?.
Next challenges:
Nested List Weight Sum II
Freedom Trail
Parallel Courses II
Show off your acceptance:
"""
