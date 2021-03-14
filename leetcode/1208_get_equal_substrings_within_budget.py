class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        cost, left, max_len = 0, 0, 0
        for right in range(n):
            cost += abs(ord(s[right])-ord(t[right]))
            while cost > maxCost:
                cost -= abs(ord(s[left])-ord(t[left]))
                left += 1
            max_len = max(max_len, right-left+1)
        return max_len


"""
Success
Details 
Runtime: 136 ms, faster than 15.53% of Python3 online submissions for Get Equal Substrings Within Budget.
Memory Usage: 14.9 MB, less than 70.55% of Python3 online submissions for Get Equal Substrings Within Budget.
Next challenges:
Maximal Rectangle
Counting Elements
Find Winner on a Tic Tac Toe Game
"""
