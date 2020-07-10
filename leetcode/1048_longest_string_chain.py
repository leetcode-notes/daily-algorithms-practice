class Solution:
    def longestStrChain(self, words) -> int:
        words.sort(key=len)
        dp = {word: 1 for word in words}
        longest = 1
        for word in words:
            for i in range(len(word)):
                predecessor = word[:i] + word[i+1:]
                if predecessor in dp:
                    dp[word] = max(dp[word], dp[predecessor] + 1)
                    longest = max(longest, dp[word])
        return longest


'''
Success
Details
Runtime: 192 ms, faster than 53.05% of Python3
Memory Usage: 14.1 MB, less than 61.60% of Python3
Next challenges:
Can I Win
Cherry Pickup
Soup Servings
'''
