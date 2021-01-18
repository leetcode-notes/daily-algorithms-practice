# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def isEvenOddTree(self, root) -> bool:
        queue = deque([root])
        res = []
        while queue:
            qlength = len(queue)
            temp = []
            for _ in range(qlength):
                cur = queue.popleft()
                temp.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(temp)
        for i, level in enumerate(res):
            if i % 2 == 0:
                for j in range(len(level)):
                    if level[j] % 2 != 1:
                        return False
                    if j > 0:
                        if level[j] <= level[j-1]:
                            return False
            else:
                for j in range(len(level)):
                    if level[j] % 2 != 0:
                        return False
                    if j > 0:
                        if level[j] >= level[j-1]:
                            return False
        return True


"""Success
Details 
Runtime: 528 ms, faster than 52.52% of Python3 online submissions for Even Odd Tree.
Memory Usage: 45.9 MB, less than 25.21% of Python3 online submissions for Even Odd Tree.
Next challenges:
Binary Tree Preorder Traversal
Count Complete Tree Nodes
Sum of Distances in Tree"""
