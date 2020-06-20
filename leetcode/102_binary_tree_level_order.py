# Definition for a binary tree node.
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        res = []
        while queue:
            qlength = len(queue)
            cur_level = []
            for _ in range(qlength):
                cur_node = queue.popleft()
                cur_level.append(cur_node.val)
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            res.append(cur_level)
        return res


'''
Success
Details
Runtime: 32 ms, faster than 81.51% of Python3
Memory Usage: 14 MB, less than 71.29% of Python3
Next challenges:
Binary Tree Zigzag Level Order Traversal
Binary Tree Level Order Traversal II
Minimum Depth of Binary Tree
Binary Tree Vertical Order Traversal
Average of Levels in Binary Tree
N-ary Tree Level Order Traversal
Cousins in Binary Tree
'''
