class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}

        for c1, c2 in zip(s, t):
            if c1 not in s_to_t and c2 not in t_to_s:
                s_to_t[c1] = c2
                t_to_s[c2] = c1
            elif s_to_t.get(c1) != c2 or t_to_s.get(c2) != c1:
                return False
        return True


"""
Success
Details 
Runtime: 44 ms, faster than 53.18% of Python3 online submissions for Isomorphic Strings.
Memory Usage: 14.2 MB, less than 88.03% of Python3 online submissions for Isomorphic Strings.
Next challenges:
Longest Substring with At Least K Repeating Characters
Complex Number Multiplication
Design A Leaderboard
"""
