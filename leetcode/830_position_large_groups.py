class Solution:
    def largeGroupPositions(self, s: str):
        start, count, res = 0, 1, []
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                if count >= 3:
                    res.append([start, i-1])
                start = i
                count = 1
            else:
                count += 1
        if count >= 3:
            res.append([start, i])
        return res


'''
Success
Details
Runtime: 36 ms, faster than 78.24% of Python3 online 
submissions
for Positions of Large Groups.
Memory Usage: 14.1 MB, less than 87.71% of 
Python3 online submissions for Positions of Large Groups.
Next challenges:
Search in Rotated Sorted Array
Range Addition
Max Consecutive Ones
'''
