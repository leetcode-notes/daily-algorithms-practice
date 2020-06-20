from collections import deque


class Solution:
    def findBottomLeftValue(self, root) -> int:
        if not root:
            return -1
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
        return res[-1][0]


'''
Success
Details
Runtime: 48 ms, faster than 50.49% of Python3
Memory Usage: 15.9 MB, less than 94.32% of Python3
Next challenges:
Range Sum of BST
Sum of Nodes with Even-Valued Grandparent
Minimum Time to Collect All Apples in a Tree
'''
