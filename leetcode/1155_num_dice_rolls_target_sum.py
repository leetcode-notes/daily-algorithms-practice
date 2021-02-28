"""
number of ways (sequences of rolls) to make target with 1 die that has faces 1....f
"""


def numWays(f, target):
    if target == 0:
        return 0

    num_ways = 0
    for i in range(1, f+1):
        if i == target:
            num_ways += 1
        elif i < target:
            num_ways += numWays(f, target-i)
    return num_ways


def numWaysDp(f, target):
    dp = [0]*(target+1)
    dp[0] = 0
    for i in range(1, target+1):
        for j in range(1, f+1):
            if j == i:
                dp[i] += 1
            elif j < i:
                dp[i] += dp[i-j]
    return dp[-1]


def numRollsToTarget(d, f, target):
    """
    throw d dice with faces numbered 1 to f. how many combinations of faces showing sum to target
    say on the nth die, we see face value j, then numWays(n, f, target) = numWays(n-1, f, target-j)
    """
    dp = [[0]*(target+1) for _ in range(d+1)]
    dp[0][0] = 0
    for f in range(1, f+1):
        for n in range(1, target+1):
            if f == n:
                dp[1][n] = 1

    for i in range(2, d+1):
        for j in range(1, target+1):
            for k in range(1, f+1):
                if k > j:
                    continue
                else:
                    dp[i][j] += dp[i-1][j-k]
    return dp[d][target] % (10**9+7)


class Solution:
    def numRollsToTarget(self, d, f, target):
        """
        throw d dice with faces numbered 1 to f. how many combinations of faces showing sum to target
        say on the nth die, we see face value j, then numWays(n, f, target) = numWays(n-1, f, target-j)
        """
        dp = [[0]*(target+1) for _ in range(d+1)]
        dp[0][0] = 0
        for f in range(1, f+1):
            if f <= target:
                dp[1][f] = 1

        for i in range(2, d+1):
            for j in range(1, target+1):
                for k in range(1, f+1):
                    if k > j:
                        continue
                    else:
                        dp[i][j] += dp[i-1][j-k]
        return dp[d][target] % (10**9+7)


"""
Success
Details 
Runtime: 752 ms, faster than 29.93% of Python3 online submissions for Number of Dice Rolls With Target Sum.
Memory Usage: 14.6 MB, less than 78.45% of Python3 online submissions for Number of Dice Rolls With Target Sum.
Next challenges:
Super Washing Machines
Minimum Cost Tree From Leaf Values
Minimum One Bit Operations to Make Integers Zero
"""
