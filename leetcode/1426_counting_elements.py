class Solution:
    def countElements(self, arr):
        count, d = 0, set()
        for n in arr:
            d.add(n)
        for n in arr:
            if n+1 in d:
                count += 1
        return count


"""
Success
Details 
Runtime: 44 ms, faster than 39.65% of Python3 online submissions for Counting Elements.
Memory Usage: 14.2 MB, less than 75.44% of Python3 online submissions for Counting Elements.
Next challenges:
Best Time to Buy and Sell Stock III
1-bit and 2-bit Characters
Design Most Recently Used Queue
"""
