class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        max_depth = 0
        for c in s:
            if c == '(':
                stack.append('(')
            elif c == ')':
                max_depth = max(max_depth, len(stack))
                stack.pop()
        return max_depth


"""
Success
Details
Runtime: 32 ms, faster than 56.80% of Python3 online submissions
for Maximum Nesting Depth of the Parentheses.
Memory Usage: 14.2 MB, less than 66.07% of Python3 online submissions
for Maximum Nesting Depth of the Parentheses.
Next challenges:
Maximum Nesting Depth of Two Valid Parentheses Strings
"""
