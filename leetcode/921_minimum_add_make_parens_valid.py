class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack = []
        count = 0
        for c in S:
            if c == "(":
                stack.append("(")
            else:
                if len(stack) < 1:
                    count += 1
                else:
                    stack.pop()
        return count + len(stack)


"""
Success
Details 
Runtime: 56 ms, faster than 6.75% of Python3 online submissions for Minimum Add to Make Parentheses Valid.
Memory Usage: 14.3 MB, less than 14.71% of Python3 online submissions for Minimum Add to Make Parentheses Valid.
Next challenges:
Broken Calculator
Longest Happy String
Minimum Deletions to Make String Balanced
"""
