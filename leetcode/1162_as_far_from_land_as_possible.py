from collections import deque
from typing import Deque


class Solution:
    def maxDistance(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        queue: Deque = deque([])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))

        ans = -1
        step = 1
        while queue:
            qlength = len(queue)
            for _ in range(qlength):
                r, c = queue.popleft()
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 0:
                        grid[nr][nc] = step
                        queue.append((nr, nc))
            step += 1
        for i in range(m):
            for j in range(n):
                ans = max(grid[i][j], ans)
        return ans if ans > 1 else -1


'''
Success
Details
Runtime: 592 ms, faster than 78.03% of Python3
Memory Usage: 14.3 MB, less than 79.45% of Python3
Shortest Distance from All Buildings
'''
