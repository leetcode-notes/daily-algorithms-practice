class Solution:
    def checkIfCanBreak(self, s1, s2) -> bool:
        if len(s1) != len(s2):
            return False
        s1 = sorted(s1)
        s2 = sorted(s2)
        a, b = True, True
        for c, d in zip(s1, s2):
            if ord(c) < ord(d):
                a = False
            if ord(d) < ord(c):
                b = False
        return a or b
            