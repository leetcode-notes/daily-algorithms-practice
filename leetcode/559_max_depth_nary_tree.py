class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        height = 0
        for node in root.children:
            height = max(self.maxDepth(node), height)
        return height + 1


'''
Success
Details
Runtime: 52 ms, faster than 30.42% of Python3
Memory Usage: 15.9 MB, less than 5.09% of Python3
Next challenges:
Maximum Depth of Binary Tree
'''
