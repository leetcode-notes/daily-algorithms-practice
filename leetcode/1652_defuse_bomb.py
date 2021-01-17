class Solution:
    def decrypt(self, code, k: int):
        n = len(code)
        res = []
        if k == 0:
            return [0]*len(code)
        if k < 0:
            for i in range(n):
                cur = 0
                for j in range(k, 0):
                    idx = (i+j)
                    cur += code[idx]
                res.append(cur)
            return res
        if k > 0:
            for i in range(n):
                cur = 0
                for j in range(1, k+1):
                    idx = (i+j) % n
                    cur += code[idx]
                res.append(cur)
            return res


"""
Success
Details
Runtime: 52 ms, faster than 37.83% of Python3 
online submissions for Defuse the Bomb.
Memory Usage: 14.3 MB, less than 32.34% of Python3 online
submissions for Defuse the Bomb.
Next challenges:
Array Nesting
Maximum Average Subarray II
Pour Water
Show off your acceptance:
"""
