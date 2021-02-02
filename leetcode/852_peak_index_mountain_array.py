class Solution:
    def peakIndexInMountainArray(self, arr):
        for i in range(1, len(arr)-1):
            if arr[i-1] < arr[i] > arr[i+1]:
                return i


"""
Success
Details 
Runtime: 76 ms, faster than 62.35% of Python3 online submissions for Peak Index in a Mountain Array.
Memory Usage: 15.4 MB, less than 12.58% of Python3 online submissions for Peak Index in a Mountain Array.
Next challenges:
Find in Mountain Array
"""
