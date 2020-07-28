class Solution:
    def sumNumbers(self, root) -> int:

        def dfs(root, cur_sum):
            if not root:
                return 0
            cur_sum = cur_sum*10+root.val
            if not root.left and not root.right:
                return cur_sum
            return dfs(root.left, cur_sum) + dfs(root.right, cur_sum)

        return dfs(root, 0)


'''
Runtime: 44 ms, faster than 24.41% of Python3
Memory Usage: 13.8 MB, less than 96.10% of Python3
Next challenges:
Binary Tree Maximum Path Sum
'''
