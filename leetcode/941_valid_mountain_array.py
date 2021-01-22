class Solution:
    def validMountainArray(self, arr) -> bool:
        peak = max(arr)
        peak_index = arr.index(peak)
        if peak_index == 0 or peak_index == len(arr)-1:
            return False
        for i in range(peak_index+1):
            if i > 0:
                if arr[i] <= arr[i-1]:
                    return False
        for i in range(peak_index+1, len(arr)):
            if i > 0:
                if arr[i] >= arr[i-1]:
                    return False
        return True


"""
Success
Details 
Runtime: 200 ms, faster than 71.59% of Python3 online submissions for Valid Mountain Array.
Memory Usage: 15.7 MB, less than 11.18% of Python3 online submissions for Valid Mountain Array.
Next challenges:
Maximal Rectangle
Circular Array Loop
Maximum Sum Circular Subarray
Show off your acceptance:
"""
