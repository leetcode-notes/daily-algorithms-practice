from collections import deque


class Solution:
    def updateMatrix(self, matrix):
        updates = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    updates[(i, j)] = self.bfs(matrix, i, j)

        for idx in updates:
            r, c = idx
            matrix[r][c] = updates[idx]
        return matrix

    def bfs(self, matrix, r, c):
        visited = set()
        queue = deque([(r, c)])
        distance = 0
        while queue:
            qlength = len(queue)
            for _ in range(qlength):
                r, c = queue.popleft()
                if (r, c) in visited:
                    continue
                visited.add((r, c))
                if matrix[r][c] == 0:
                    return distance
                for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nr, nc = d[0] + r, d[1] + c
                    if 0 <= nr < len(matrix) and 0 <= nc < len(matrix[0]):
                        if (nr, nc) not in visited:
                            queue.append((nr, nc))
            distance += 1
        return -1


'''
Success
Details 
Runtime: 992 ms, faster than 24.68% of Python3 online submissions for 01 Matrix.
Memory Usage: 16.1 MB, less than 69.64% of Python3 online submissions for 01 Matrix.
Next challenges:
Validate Binary Search Tree
Shortest Distance from All Buildings
Trapping Rain Water II
'''
