class Solution:
    def numRabbits(self, answers) -> int:
        seen, res = {}, 0
        for num in answers:
            if num not in seen:
                res += 1 + num
                seen[num] = num
            else:
                seen[num] -= 1
            if seen[num] == 0:
                del seen[num]
        return res


'''
Success
Details
Runtime: 44 ms, faster than 66.67% of Python3
Memory Usage: 13.8 MB, less than 90.10% of Python3
Next challenges:
Strobogrammatic Number
Divide Array Into Increasing Sequences
Design File System
'''
