class Solution:
    def generate(self, numRows):
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        triangle = [[1], [1, 1]]
        if numRows == 2:
            return triangle
        for i in range(3, numRows+1):
            new_row = [1]
            for j in range(1, len(triangle[i-2])):
                temp = triangle[i-2][j] + triangle[i-2][j-1]
                new_row.append(temp)
            new_row.append(1)
            triangle.append(new_row)
        return triangle


"""
Success
Details 
Runtime: 28 ms, faster than 85.49% of Python3 online submissions for Pascal's Triangle.
Memory Usage: 14.5 MB, less than 28.58% of Python3 online submissions for Pascal's Triangle.
Next challenges:
Pascal's Triangle II
"""
