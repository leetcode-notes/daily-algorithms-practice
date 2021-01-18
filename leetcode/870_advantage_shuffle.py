from collections import defaultdict


class Solution:
    def advantageCount(self, A, B):
        A = sorted(A)
        d = defaultdict(list)
        for b in sorted(B, reverse=True):
            if b < A[-1]:
                d[b].append(A.pop())
        res = []
        for b in B:
            if b in d and len(d[b]) > 0:
                res.append(d[b].pop())
            else:
                res.append(A.pop())
        return res


'''
Success
Details
Runtime: 388 ms, faster than 75.16%...
Memory Usage: 16.9 MB, less than 33.34%...
Next challenges:
Insert Delete GetRandom O(1)
Split Array into Consecutive Subsequences
Partition Labels
'''
