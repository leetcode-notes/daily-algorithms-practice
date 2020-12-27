from collections import deque


class Solution:
    def countServers(self, grid) -> int:
        seen = set()

        def bfs(grid, r, c):
            queue = deque([(r, c)])
            count = 1
            seen.add((r, c))
            while queue:
                row, col = queue.popleft()
                for i in range(len(grid)):
                    if grid[i][col] == 1 and (i, col) not in seen:
                        seen.add((i, col))
                        queue.append((i, col))
                        count += 1
                for j in range(len(grid[0])):
                    if grid[row][j] == 1 and (row, j) not in seen:
                        seen.add((row, j))
                        queue.append((row, j))
                        count += 1
            return count
        total = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in seen:
                    n = bfs(grid, i, j)
                    if n > 1:
                        total += n
        return total


"""
Success
Details
Runtime: 896 ms, faster than 6.39% of Python3 online submissions
 for Count Servers that Communicate.
Memory Usage: 16.3 MB, less than 7.89% of
Python3 online submissions for Count Servers that Communicate.
Next challenges:
Number of Connected Components in an Undirected Graph
String Transforms Into Another String
Online Majority Element In Subarray
"""
