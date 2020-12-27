class Solution:
    def replaceElements(self, arr):
        cur, prev = arr[-1], arr[-1]
        for i in range(len(arr)-2, -1, -1):
            if arr[i] > cur:
                cur = arr[i]
            arr[i] = prev
            prev = cur
        arr[-1] = -1
        return arr


"""
Success
Details
Runtime: 104 ms, faster than 99.62% of
Python3 online submissions for Replace Elements with
Greatest Element on Right Side.
Memory Usage: 15.4 MB, less than 30.93% of
Python3 online submissions for Replace Elements with
 Greatest Element on Right Side.
Next challenges:
Valid Triangle Number
1-bit and 2-bit Characters
Most Visited Sector in a Circular Track
"""
