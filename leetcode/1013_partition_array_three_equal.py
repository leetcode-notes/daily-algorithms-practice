class Solution:
    def canThreePartsEqualSum(self, arr]) -> bool:
        total= sum(arr)
        if total % 3 != 0:
            return False
        target= total // 3
        prefs= []
        for i, n in enumerate(arr):
            if i == 0:
                prefs.append(n)
            else:
                prefs.append(prefs[-1]+n)
        i, j= 0, len(arr)-1
        while i + 1 < j:
            left, middle, right = prefs[i], prefs[j-1] -
                prefs[i], prefs[-1]-prefs[j-1]
            if left == middle == right:
                return True
            if left == target:
                j -= 1
                continue
            if right == target:
                i += 1
                continue
            else:
                i += 1
                j -= 1
        return False


"""
Success
Details
Runtime: 324 ms, faster than 28.05% of Python3 online submissions for Partition Array Into Three Parts With Equal Sum.
Memory Usage: 21.1 MB, less than 60.88% of Python3 online submissions for Partition Array Into Three Parts With Equal Sum.
Next challenges:
Word Ladder II
Contains Duplicate
Range Addition
"""
