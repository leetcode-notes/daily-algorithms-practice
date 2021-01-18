class Solution:
    def shortestToChar(self, S: str, C: str):
        res = [None for _ in range(len(S))]
        closest = None
        for i, ch in enumerate(S):
            if ch == C:
                closest = i
            if closest != None:
                res[i] = i-closest
        closest = None
        for i in range(len(S)-1, -1, -1):
            if S[i] == C:
                closest = i
            if closest != None:
                if res[i] != None:
                    res[i] = min(closest-i, res[i])
                else:
                    res[i] = closest - i
        return res


"""
Success
Details
Runtime: 40 ms, faster than 74.23% of Python3 online submissions for Shortest Distance to a Character.
Memory Usage: 14.5 MB, less than 5.46% of Python3 online submissions for Shortest Distance to a Character.
Next challenges:
Minimum Area Rectangle
Adding Two Negabinary Numbers
String Compression II
Show off your acceptance:
"""
