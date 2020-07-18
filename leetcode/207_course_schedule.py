from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        preReqs, postReqs = defaultdict(set), defaultdict(set)
        for p in prerequisites:
            preReqs[p[0]].add(p[1])
            postReqs[p[1]].add(p[0])

        sources = deque([])
        for i in range(numCourses):
            if i not in preReqs:
                sources.append(i)
        taken = []
        while sources:
            cur = sources.popleft()
            taken.append(cur)
            for node in postReqs[cur]:
                preReqs[node].remove(cur)
                if not preReqs[node]:
                    sources.append(node)
        return len(taken) == numCourses


'''
Success
Details
Runtime: 136 ms, faster than 34.66% of Python3
Memory Usage: 15.5 MB, less than 59.88% of Python3
Next challenges:
Course Schedule II
Graph Valid Tree
Minimum Height Trees
Course Schedule III
'''
