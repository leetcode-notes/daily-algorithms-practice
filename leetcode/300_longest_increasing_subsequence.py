class Solution:
    def lengthOfLIS(self, nums) -> int:
        if not nums:
            return 0
        dp = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1+dp[j])

        return max(dp)


'''
Success
Details
Runtime: 1232 ms, faster than 34.28% of Python3
Memory Usage: 13.9 MB, less than 85.27% of Python3
Next challenges:
Increasing Triplet Subsequence
Russian Doll Envelopes
Maximum Length of Pair Chain
Number of Longest Increasing Subsequence
Minimum ASCII Delete Sum for Two Strings
'''
