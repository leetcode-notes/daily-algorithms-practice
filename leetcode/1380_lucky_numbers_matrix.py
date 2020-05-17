from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        col_max = {}
        row_min = {}
        for i, row in enumerate(matrix):
            row_min[i] = min(row)
        for j in range(len(matrix[0])):
            cur_max = 0
            for row in matrix:
                if row[j] > cur_max:
                    cur_max = row[j]
            col_max[j] = cur_max
        res = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                cur_num = matrix[i][j]
                if cur_num == col_max[j] and cur_num == row_min[i]:
                    res.append(cur_num)
        return res
