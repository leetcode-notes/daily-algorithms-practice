# Definition for a binary tree node.
class Solution:
    def removeLeafNodes(self, root, target: int):
        if not root:
            return None
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        if not root.left and not root.right and root.val == target:
            return None
        return root


'''
Success
Details
Runtime: 48 ms, faster than 91.91% of Python3
Memory Usage: 14 MB, less than 84.19% of Python3
Next challenges:
Inorder Successor in BST
Inorder Successor in BST II
Second Minimum Node In a Binary Tree
'''
