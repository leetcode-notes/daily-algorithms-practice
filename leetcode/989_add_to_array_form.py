class Solution:
    def addToArrayForm(self, A, K: int):
        digits, res = [], []
        while K > 0:
            digits.append(K % 10)
            K //= 10
        cur, i, carry = len(A)-1, 0, 0
        while cur >= 0:
            if i < len(digits):
                cur_digit = digits[i]+A[cur] + carry
                if cur_digit >= 10:
                    cur_digit = cur_digit % 10
                    carry = 1
                else:
                    carry = 0
                i += 1
            else:
                cur_digit = A[cur] + carry
                if cur_digit >= 10:
                    cur_digit = cur_digit % 10
                    carry = 1
                else:
                    carry = 0
            cur -= 1
            res.append(cur_digit)
        if i < len(digits):
            for dig in digits[i:]:
                dig += carry
                if dig >= 10:
                    dig = dig % 10
                    carry = 1
                else:
                    carry = 0
                res.append(dig)
        if carry:
            res.append(1)
        return res[::-1]


"""
Success
Details 
Runtime: 284 ms, faster than 81.28% of Python3 online submissions for Add to Array-Form of Integer.
Memory Usage: 15.1 MB, less than 70.70% of Python3 online submissions for Add to Array-Form of Integer.
Next challenges:
Plus One
Add Binary
Add Strings
"""
