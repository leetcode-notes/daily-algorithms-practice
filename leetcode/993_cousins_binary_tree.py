# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int):

        x_parent, x_depth = self.dfs(root, root, x)
        y_parent, y_depth = self.dfs(root, root,  y)
        if x_parent != y_parent and x_depth == y_depth:
            return True
        return False

    def dfs(self, root, parent, val, depth=0):
        if not root:
            return []
        if root.val == val:
            return [parent.val, depth]
        return self.dfs(root.left, root, val, depth+1) or self.dfs(root.right, root, val, depth+1)


t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
t.left.right = TreeNode(4)


s = Solution()
print(s.isCousins(t, 2, 3))

'''
Success
Details
Runtime: 28 ms, faster than 87.74% of Python3...
Memory Usage: 13.8 MB, less than 49.32% of Python3...
Next challenges:
Binary Tree Zigzag Level Order Traversal
Construct Binary Tree from Preorder and Inorder Traversal
Binary Tree Level Order Traversal II
'''
