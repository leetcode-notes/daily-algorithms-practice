from collections import defaultdict


class Solution:
    def kWeakestRows(self, mat, k):
        strength = defaultdict(list)
        for i, row in enumerate(mat):
            count = 0
            for n in row:
                if n == 1:
                    count += 1
                else:
                    break
            strength[count].append(i)
        min_strength = 0
        res = []
        while min_strength <= len(mat[0]):
            if min_strength in strength:
                for idx in sorted(strength[min_strength]):
                    if k == 0:
                        return res
                    res.append(idx)
                    k -= 1
            min_strength += 1
        return res


mat = [[1, 1, 0, 0, 0],
       [1, 1, 1, 1, 0],
       [1, 0, 0, 0, 0],
       [1, 1, 0, 0, 0],
       [1, 1, 1, 1, 1]]
k = 3


mat1 = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]
k1 = 1

mat2 = [[1, 0], [1, 0], [1, 0], [1, 1]]
k2 = 4
s = Solution()
print(s.kWeakestRows(mat2, k2))

'''
Success
Details
Runtime: 112 ms, faster than 74.67% of Python3...
Memory Usage: 14 MB, less than 59.30% of Python3..
Next challenges:
Rotate Image
Find Minimum in Rotated Sorted Array II
Shortest Word Distance III
'''
