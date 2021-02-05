class Solution:
    def getAllElements(self, root1, root2):
        tree1_vals = []
        tree2_vals = []

        def dfs(root, val_set):
            if not root:
                return
            dfs(root.left, val_set)
            val_set.append(root.val)
            dfs(root.right, val_set)
        dfs(root1, tree1_vals)
        dfs(root2, tree2_vals)
        i, j = 0, 0
        res = []
        while i < len(tree1_vals) and j < len(tree2_vals):
            if tree1_vals[i] <= tree2_vals[j]:
                res.append(tree1_vals[i])
                i += 1
            else:
                res.append(tree2_vals[j])
                j += 1
        while i < len(tree1_vals):
            res.append(tree1_vals[i])
            i += 1
        while j < len(tree2_vals):
            res.append(tree2_vals[j])
            j += 1

        return res


"""
Success
Details 
Runtime: 492 ms, faster than 25.43% of Python3 online submissions for All Elements in Two Binary Search Trees.
Memory Usage: 22.8 MB, less than 18.11% of Python3 online submissions for All Elements in Two Binary Search Trees.
Next challenges:
Intersection of Two Arrays II
Maximum Number of Ones
Lowest Common Ancestor of a Binary Tree III
"""
