class Solution:
    def reformat(self, s: str) -> str:
        a, b = 0, 0
        digits, strs = [], []
        if len(s) == 1:
            return s
        for c in s:
            if c.isdigit():
                a += 1
                digits.append(c)
            else:
                b += 1
                strs.append(c)
        if abs(a-b) > 1:
            return ""
        res = []
        for i in range(min(len(digits), len(strs))):
            if len(digits) > len(strs):
                res.append(digits[i])
                res.append(strs[i])
            else:
                res.append(strs[i])
                res.append(digits[i])
        if i < len(digits)-1:
            res.append(digits[-1])
        if i < len(strs)-1:
            res.append(strs[-1])
        return "".join(c for c in res)


s = Solution()
print(s.reformat("ase1293"))
