from collections import Counter


class Solution:
    def __init__(self):
        self.paths = []

    def pseudoPalindromicPaths(self, root):
        self.dfs(root, "")
        count = 0
        for path in self.paths:
            if self.is_palindromic(path):
                count += 1
        return count

    def dfs(self, node, path):
        if not node:
            return
        path += str(node.val)
        if not node.left and not node.right:
            self.paths.append(path)
            return
        self.dfs(node.left, path)
        self.dfs(node.right, path)

    def is_palindromic(self, path):
        c = Counter(path)
        odds = 0
        for k, v in c.items():
            if v % 2 == 1:
                odds += 1
        if odds == 1 or odds == 0:
            return True
        else:
            return False
