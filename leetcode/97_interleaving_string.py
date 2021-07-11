from collections import deque


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        a, b = len(s1), len(s2)
        if len(s3) != a + b:
            return False
        queue = deque()
        queue.append((0, 0))
        visited = set()

        while queue:
            r, c = queue.popleft()
            if r + c == len(s3):
                return True

            if r < len(s1) and (r+1, c) not in visited and s3[r+c] == s1[r]:
                queue.append((r+1, c))
                visited.add((r+1, c))

            if c < len(s2) and (r, c+1) not in visited and s3[r+c] == s2[c]:
                queue.append((r, c+1))
                visited.add((r, c+1))
        return False


class SolutionDP:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        r, c, t = len(s1), len(s2), len(s3)
        if r + c != t:
            return False

        dp = [[True]*(c+1) for _ in range(r+1)]

        for i in range(1, r+1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]

        for j in range(1, c+1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]

        for i in range(1, r+1):
            for j in range(1, c+1):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]
                            ) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])

        return dp[-1][-1]


"""
Success
Details 
Runtime: 36 ms, faster than 82.80% of Python3 online submissions for Interleaving String.
Memory Usage: 14.4 MB, less than 60.93% of Python3 online submissions for Interleaving String.
Next challenges:
Largest Divisible Subset
Minimum Window Subsequence
Minimum Sideway Jumps
"""

"""
Success
Details 
Runtime: 68 ms, faster than 16.01% of Python3 online submissions for Interleaving String.
Memory Usage: 15.3 MB, less than 8.33% of Python3 online submissions for Interleaving String.
Next challenges:
Word Squares
Dota2 Senate
Count Number of Homogenous Substrings
"""
