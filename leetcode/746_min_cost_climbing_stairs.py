class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        memo = [0]*len(cost)
        memo[0] = cost[0]
        memo[1] = cost[1]
        for i in range(2, len(cost)):
            memo[i] = cost[i] + min(memo[i-1], memo[i-2])
        return min(memo[-1], memo[-2])


"""
Success
Details 
Runtime: 52 ms, faster than 91.07% of Python3 online submissions for Min Cost Climbing Stairs.
Memory Usage: 14.2 MB, less than 90.48% of Python3 online submissions for Min Cost Climbing Stairs.
Next challenges:
Construct Binary Tree from Preorder and Inorder Traversal
Rotate Array
Race Car
"""
