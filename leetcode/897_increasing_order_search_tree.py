import TreeNode


class Solution:
    def increasingBST(self, root):
        res = []

        def dfs(root):
            if not root:
                return None
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        dfs(root)
        dummy = ret = TreeNode(res[0])
        for v in res[1:]:
            ret.right = TreeNode(v)
            ret = ret.right
        return dummy


"""
Success
Details 
Runtime: 20 ms, faster than 99.36% of Python3 online submissions for Increasing Order Search Tree.
Memory Usage: 14.5 MB, less than 7.17% of Python3 online submissions for Increasing Order Search Tree.
Next challenges:
Closest Binary Search Tree Value II
Clone Binary Tree With Random Pointer
Lexicographically Smallest String After Applying Operations
"""
