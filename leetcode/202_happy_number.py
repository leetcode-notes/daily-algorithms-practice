class Solution:
    def isHappy(self, n: int):
        seen = set()
        while n:
            if n == 1:
                return True
            if n in seen:
                return False
            seen.add(n)
            temp = n
            cur_sum = 0
            while temp:
                digit = temp % 10
                cur_sum += digit**2
                temp //= 10
            n = cur_sum


"""
Success
Details 
Runtime: 24 ms, faster than 99.23% of Python3 online submissions for Happy Number.
Memory Usage: 14.3 MB, less than 51.52% of Python3 online submissions for Happy Number.
Next challenges:
Linked List Cycle
Add Digits
Ugly Number
"""
