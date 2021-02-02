class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = [0]
        for par in S:
            if par == "(":
                stack.append(0)
            else:
                last = stack.pop()
                if last == 0:
                    score = 1
                else:
                    score = last*2
                stack[-1] += score
        return stack[0]


"""
Success
Details 
Runtime: 32 ms, faster than 53.99% of Python3 online submissions for Score of Parentheses.
Memory Usage: 14.1 MB, less than 74.92% of Python3 online submissions for Score of Parentheses.
Next challenges:
Count and Say
Expressive Words
Check If Word Is Valid After Substitutions
"""


class Solution2:
    def scoreOfParentheses(self, S: str) -> int:
        stack = [0]
        for c in S:
            if c == "(":
                stack.append(0)
            elif c == ")":
                last = stack.pop()
                if last == 0:
                    score = 1
                else:
                    score = 2*last
                stack[-1] += score
        return stack[-1]


"""
Success
Details 
Runtime: 48 ms, faster than 7.65% of Python3 online submissions for Score of Parentheses.
Memory Usage: 14.2 MB, less than 45.60% of Python3 online submissions for Score of Parentheses.
Next challenges:
Binary Tree Postorder Traversal
Palindrome Pairs
Number of Valid Subarrays
"""
