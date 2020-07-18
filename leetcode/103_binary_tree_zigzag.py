from collections import deque


class Solution:
    def zigzagLevelOrder(self, root):
        left = True
        if not root:
            return []
        queue, res = deque([root]), []
        while queue:
            qlength = len(queue)
            level = []
            for _ in range(qlength):
                cur = queue.popleft()
                level.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            if not left:
                level = level[::-1]
            left = not left
            res.append(level)
        return res


'''
Success
Details
Runtime: 44 ms, faster than 28.51% of Python3
Memory Usage: 14.1 MB, less than 34.81% of Python3
Next challenges:
All Nodes Distance K in Binary Tree
Construct Binary Tree from Preorder and Postorder Traversal
Check if There is a Valid Path in a Grid
'''
