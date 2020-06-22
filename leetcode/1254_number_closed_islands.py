'''
modified version of Jun's solution
'''
import collections
DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


class Solution:
    def closedIsland(self, grid):
        if not grid or not grid[0]:
            return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 or j == 0 or i == len(grid)-1 or j == len(grid[0])-1:
                    if grid[i][j] == 0:
                        self.bfs(grid, i, j)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    self.bfs(grid, i, j)
                    count += 1
        return count

    def bfs(self, grid, x, y):
        queue = collections.deque([(x, y)])
        grid[x][y] = 1
        while queue:
            x, y = queue.popleft()
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]):
                    continue
                if grid[nx][ny] == 0:
                    queue.append((nx, ny))
                    grid[nx][ny] = 1


'''
Success
Details
Runtime: 148 ms, faster than 54.80% of Python3...
Memory Usage: 14 MB, less than 84.46% of Python3...
Next challenges:
Clone Graph
Leaf-Similar Trees
Frog Position After T Seconds
'''
