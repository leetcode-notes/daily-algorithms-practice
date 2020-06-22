from collections import deque


class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        res = []
        queue = deque([root])
        while queue:
            qlength = len(queue)
            temp = []
            for _ in range(qlength):
                cur_node = queue.popleft()
                temp.append(cur_node.val)
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            res.append(temp[-1])
        return res


'''
Success
Details
Runtime: 36 ms, faster than 42.27% of Python3
Memory Usage: 13.5 MB, less than 99.95% of Python3
Next challenges:
Populating Next Right Pointers in Each Node
Boundary of Binary Tree
'''
