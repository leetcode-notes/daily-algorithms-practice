class Solution:
    def diagonalSum(self, mat) -> int:
        total = 0
        start = 0
        for i in range(len(mat)):
            total += mat[i][start]
            start += 1
        mid = len(mat)//2
        even = False
        if len(mat) % 2 == 0:
            even = True
        start = 0
        for i in range(len(mat)-1, -1, -1):
            total += mat[i][start]
            start += 1
        if not even:
            total -= mat[mid][mid]
        return total


"""
Success
Details
Runtime: 104 ms, faster than 76.57% of 
Python3 online submissions for Matrix Diagonal Sum.
Memory Usage: 14.6 MB, less than 10.30% of Python3 online
submissions for Matrix Diagonal Sum.
Next challenges:
Median of Two Sorted Arrays
Longest Line of Consecutive One in Matrix
Maximum Distance in Arrays
"""
