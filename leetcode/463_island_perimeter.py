from typing import List


class Solution:
    # for each land square count number of edges and add to runniing sum
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    perimeter += self.countEdges([i, j], grid)
        return perimeter

    def countEdges(self, cell: List[int], grid: List[List[int]]) -> int:
        r, c = cell[0], cell[1]
        edges = 0
        if r == 0:
            edges += 1
        if c == 0:
            edges += 1
        if r == len(grid)-1:
            edges += 1
        if c == len(grid[0])-1:
            edges += 1

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for d in directions:
            nr, nc = r+d[0], c + d[1]
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                if grid[nr][nc] == 0:
                    edges += 1

        return edges


test1 = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
s = Solution()
print(s.islandPerimeter(test1))


'''
Success
Details
Runtime: 716 ms, faster than 29.42% of Python...
Memory Usage: 14.1 MB, less than 39.39% of Python3...
Next challenges:
Coloring A Border
'''
