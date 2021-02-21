from collections import defaultdict


class Solution:
    def canCross(self, stones) -> bool:
        d = defaultdict(set)
        d[0].add(0)
        for i in range(len(stones)):
            if stones[i] in d:
                for step_size in d[stones[i]]:
                    if step_size > 0:
                        d[stones[i]+step_size].add(step_size)
                    if step_size > 1:
                        d[stones[i]+step_size-1].add(step_size-1)
                    d[stones[i]+step_size+1].add(step_size+1)
        return stones[-1] in d


"""
Success
Details 
Runtime: 220 ms, faster than 62.62% of Python3 online submissions for Frog Jump.
Memory Usage: 16.6 MB, less than 62.79% of Python3 online submissions for Frog Jump.
Next challenges:
Encode String with Shortest Length
Shortest Path Visiting All Nodes
Maximum Non Negative Product in a Matrix
"""
