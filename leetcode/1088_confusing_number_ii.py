class Solution:
    def confusingNumberII(self, N):
        # digits that will be valid after rotation
        valid = [0, 1, 6, 8, 9]
        mapping = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}

        def rec(num, rotation, digit):
            res = 0
            if num != rotation:
                res += 1
            for i in valid:
                if i == 0 and num == 0:
                    continue
            # don't consider numbers > N
                if num*10 + i <= N:
                    res += rec(num*10+i, mapping[i]*digit+rotation, digit*10)
            return res

        return rec(0, 0, 1)
