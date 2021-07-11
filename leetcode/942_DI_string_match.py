class Solution:
    def diStringMatch(self, s: str):
        low, high = 0, len(s)
        res = []
        for ch in s:
            if ch == "I":
                res.append(low)
                low += 1
            else:
                res.append(high)
                high -= 1
        return res + [low]


"""
Success
Details 
Runtime: 80 ms, faster than 21.99% of Python3 online submissions for DI String Match.
Memory Usage: 15.2 MB, less than 41.83% of Python3 online submissions for DI String Match.
Next challenges:
One Edit Distance
Divide Array in Sets of K Consecutive Numbers
Can You Eat Your Favorite Candy on Your Favorite Day?
"""
