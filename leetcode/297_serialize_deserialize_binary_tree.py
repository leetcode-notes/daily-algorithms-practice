# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        self.data = ""

        def dfs(node):
            if node:
                self.data += "%s " % node.val
                dfs(node.left)
                dfs(node.right)
            else:
                self.data += "# "
        dfs(root)
        return self.data

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def dfs():
            val = next(data)
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
        data = iter(data.split())
        return dfs()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
"""
Success
Details 
Runtime: 132 ms, faster than 53.73% of Python3 online submissions for Serialize and Deserialize Binary Tree.
Memory Usage: 19 MB, less than 44.19% of Python3 online submissions for Serialize and Deserialize Binary Tree.
Next challenges:
Encode and Decode Strings
Serialize and Deserialize BST
Find Duplicate Subtrees
Serialize and Deserialize N-ary Tree
Show off your acceptance:
"""
