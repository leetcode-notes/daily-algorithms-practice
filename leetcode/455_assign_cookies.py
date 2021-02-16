class Solution:
    def findContentChildren(self, g, s) -> int:
        g.sort()
        s.sort()
        res = 0
        i = len(g)-1
        while s and i >= 0:
            if s[-1] >= g[i]:
                s.pop()
                res += 1
            i -= 1
        return res


"""
Success
Details 
Runtime: 152 ms, faster than 93.80% of Python3 online submissions for Assign Cookies.
Memory Usage: 15.7 MB, less than 96.96% of Python3 online submissions for Assign Cookies.
Next challenges:
Candy
IPO
Couples Holding Hands
"""
