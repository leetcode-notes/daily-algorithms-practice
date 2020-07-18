class Solution:
    def numSubmat(self, mat):
        for r, row in enumerate(mat):
            for c, v in enumerate(row):
                if c > 0 and v == 1:
                    mat[r][c] += mat[r][c-1]

        res = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                m = mat[i][j]
                for k in range(i, len(mat)):
                    m = min(m, mat[k][j])
                    res += m
        return res


'''
Success
Details
Runtime: 1580 ms, faster than 25.20% of Python3
Memory Usage: 14.2 MB, less than 100.00% of Python3
Next challenges:
Sentence Screen Fitting
Super Egg Drop
Stone Game II
'''
