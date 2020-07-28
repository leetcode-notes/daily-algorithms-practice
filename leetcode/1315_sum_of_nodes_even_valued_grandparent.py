# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def sumEvenGrandparent(self, root) -> int:
        p, gp = None, None
        queue = deque([(root, p, gp)])
        total = 0
        while queue:
            qlength = len(queue)
            for _ in range(qlength):
                cur, p, gp = queue.popleft()
                if gp is not None:
                    if gp % 2 == 0:
                        total += cur.val
                if cur.left:
                    queue.append((cur.left, cur.val, p))
                if cur.right:
                    queue.append((cur.right, cur.val, p))
        return total


'''
Success
Details
Runtime: 124 ms, faster than 40.13% of Python3
Memory Usage: 17.3 MB, less than 24.36% of Python3
Next challenges:
Sum Root to Leaf Numbers
Minimum Distance Between BST Nodes
Smallest Subtree with all the Deepest Nodes
'''
