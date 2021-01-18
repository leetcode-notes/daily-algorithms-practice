class Solution:
    def findSubsequences(self, nums):
        res = set()

        def dfs(start, sequence):
            if len(sequence) > 1:
                res.add(tuple(sequence[:]))
            for i in range(start, len(nums)):
                if not sequence or sequence[-1] <= nums[i]:
                    dfs(i+1, sequence+[nums[i]])
        dfs(0, [])
        return res


"""
Success
Details 
Runtime: 312 ms, faster than 26.12% of Python3 online submissions for Increasing Subsequences.
Memory Usage: 22.7 MB, less than 38.16% of Python3 online submissions for Increasing Subsequences.
Next challenges:
Shopping Offers
Flatten a Multilevel Doubly Linked List
Increasing Order Search Tree
"""
