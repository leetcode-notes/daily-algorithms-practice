from collections import defaultdict


class Solution:
    def groupThePeople(self, groupSizes):
        res = []
        size_to_label = defaultdict(list)
        for label, size in enumerate(groupSizes):
            size_to_label[size].append(label)
        for size, group in size_to_label.items():
            start = 0
            while start < len(group):
                res.append(group[start:start+size])
                start += size
        return res


"""
Success
Details 
Runtime: 68 ms, faster than 96.71% of Python3 online submissions for Group the People Given the Group Size They Belong To.
Memory Usage: 14.3 MB, less than 74.79% of Python3 online submissions for Group the People Given the Group Size They Belong To.
Next challenges:
Meeting Rooms II
Divide Array in Sets of K Consecutive Numbers
Maximum Non Negative Product in a Matrix
"""
