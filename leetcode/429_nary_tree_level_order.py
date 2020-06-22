from collections import deque


class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        queue = deque([root])
        res = []
        while queue:
            qlength = len(queue)
            temp = []
            for _ in range(qlength):
                cur_node = queue.popleft()
                temp.append(cur_node.val)
                if cur_node.children:
                    for c in cur_node.children:
                        queue.append(c)
            res.append(temp)
        return res


'''
Success
Details
Runtime: 56 ms, faster than 54.51% of Python3
Memory Usage: 15.7 MB, less than 35.21% of Python3
Next challenges:
N-ary Tree Preorder Traversal
N-ary Tree Postorder Traversal
'''
