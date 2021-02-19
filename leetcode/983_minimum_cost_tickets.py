class Solution:
    def mincostTickets(self, days, costs) -> int:
        dp = {}
        for i in range(366):
            dp[i] = -1
        dp[0] = 0
        for day in days:
            dp[day] = 0

        for i in range(1, 366):
            if dp[i] == -1:
                dp[i] = dp[i-1]
            else:
                dp[i] = min(dp.get(i-1, 0)+costs[0], dp.get(i-7, 0) +
                            costs[1], dp.get(i-30, 0)+costs[2])

        return dp[365]


"""
Success
Details 
Runtime: 40 ms, faster than 85.16% of Python3 online submissions for Minimum Cost For Tickets.
Memory Usage: 14.4 MB, less than 44.39% of Python3 online submissions for Minimum Cost For Tickets.
Next challenges:
Unique Binary Search Trees
Race Car
Number of Music Playlists
"""
