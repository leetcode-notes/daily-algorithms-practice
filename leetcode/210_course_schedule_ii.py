from collections import defaultdict, deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        preReqs, postReqs = defaultdict(set), defaultdict(set)
        for p in prerequisites:
            preReqs[p[0]].add(p[1])
            postReqs[p[1]].add(p[0])
        sources = deque([])
        for i in range(numCourses):
            if i not in preReqs:
                sources.append(i)
        course_list = []
        while sources:
            cur = sources.popleft()
            course_list.append(cur)
            for node in postReqs[cur]:
                preReqs[node].remove(cur)
                if not preReqs[node]:
                    sources.append(node)
        return course_list if len(course_list) == numCourses else []


'''
Success
Details
Runtime: 100 ms, faster than 91.55% of Python3
Memory Usage: 15.4 MB, less than 52.85% of Python3
Next challenges:
Alien Dictionary
Minimum Height Trees
Sequence Reconstruction
Course Schedule III
'''
