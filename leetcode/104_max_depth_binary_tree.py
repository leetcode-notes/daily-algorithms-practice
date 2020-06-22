class Solution:
    def maxDepth(self, root) -> int:
        if not root:
            return 0
        height = 0
        if root.left:
            height = max(height, self.maxDepth(root.left))
        if root.right:
            height = max(height, self.maxDepth(root.right))
        return height + 1


'''
Success
Details
Runtime: 40 ms, faster than 77.47% of Python3
Memory Usage: 15.5 MB, less than 30.50% of Python3
Next challenges:
Balanced Binary Tree
Minimum Depth of Binary Tree
Time Needed to Inform All Employees
'''
