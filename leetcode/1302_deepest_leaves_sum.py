from collections import deque


class Solution:
    def deepestLeavesSum(self, root) -> int:
        if not root:
            return 0
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
        return sum(res[-1])


'''
Success
Details
Runtime: 100 ms, faster than 70.22% of Python3
Memory Usage: 17.4 MB, less than 26.33% of Python3
Next challenges:
Binary Tree Level Order Traversal II
Binary Tree Longest Consecutive Sequence II
Flip Equivalent Binary Trees
'''
