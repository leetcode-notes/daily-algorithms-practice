class Solution:
    def jobScheduling(self, startTime, endTime, profit) -> int:

        jobs = list(zip(startTime, endTime, profit))
        jobs.sort()

        n = len(startTime)
        dp = [0]*n
        dp[-1] = jobs[-1][2]
        for i in range(n-2, -1, -1):
            next_job = -1
            for j in range(i+1, n):
                if jobs[j][0] >= jobs[i][1]:
                    next_job = j
                    break
            if next_job != -1:
                dp[i] = max(jobs[i][2]+dp[next_job], dp[i+1])
            else:
                dp[i] = max(jobs[i][2], dp[i+1])

        return dp[0]


"""
Success
Details 
Runtime: 544 ms, faster than 65.58% of Python3 online submissions for Maximum Profit in Job Scheduling.
Memory Usage: 26.3 MB, less than 85.68% of Python3 online submissions for Maximum Profit in Job Scheduling.
Next challenges:
Insert Interval
Minimum Number of Taps to Open to Water a Garden
Longest Palindromic Subsequence II
"""
