class Solution:
    def goodNodes(self, root) -> int:
        def dfs(root, cur_max):
            if not root:
                return 0
            ans = 0
            if root.val >= cur_max:
                cur_max = root.val
                ans += 1
            return ans + dfs(root.left, cur_max) + dfs(root.right, cur_max)
        return dfs(root, float('-inf'))


'''
Success
Details
Runtime: 260 ms, faster than 89.81% of Python3
Memory Usage: 32.3 MB, less than 92.15% of Python3
Balanced Binary Tree
Nested List Weight Sum II
Out of Boundary Paths
'''
