class Solution:
    def coinChange(self, coins, amount):

        if not amount:
            return 0

        dp = [float("inf") for i in range(amount+1)]

        for i in range(1, amount+1):
            if i in coins:
                dp[i] = 1
            else:
                for c in coins:
                    if c < i:
                        dp[i] = min(dp[i], 1+dp[i-c])
        if dp[-1] == float("inf"):
            return -1

        return dp[-1]


'''
Success
Details
Runtime: 2544 ms, faster than 10.59% of Python3
Memory Usage: 13.9 MB, less than 75.65% of Python3
Next challenges:
Minimum Cost For Tickets
'''
