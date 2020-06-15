from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        can_reach = set()
        can_reach.add(0)
        for a, b in connections:
            if b == 0:
                can_reach.add(a)

    def canReach(self, n, can_reach, reversed):
        for i in range(n):
            if i in can_reach:
                continue
            else:
                if reversed[]
