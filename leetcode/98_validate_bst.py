class Solution:
    def isValidBST(self, root) -> bool:

        def dfs(root, floor, ceil):
            if not root:
                return True
            if root.val <= floor or root.val >= ceil:
                return False
            return dfs(root.left, floor, root.val) and dfs(root.right, root.val, ceil)
        return dfs(root, -2**32, 2**32)


'''
Success
Details
Runtime: 76 ms, faster than 15.29% of Python3
Memory Usage: 16.2 MB, less than 48.20% of Python3
Next challenges:
Binary Tree Inorder Traversal
Find Mode in Binary Search Tree
'''
