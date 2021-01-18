from collections import defaultdict, deque


class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites, queries):
        prereqs = defaultdict(set)
        postreqs = defaultdict(set)
        for pre, course in prerequisites:
            prereqs[pre].add(course)
            postreqs[course].add(pre)
        res = []

        def bfs(start, end):
            queue = deque([start])
            visited = set()
            visited.add(start)
            while queue:
                cur = queue.popleft()
                if cur == end:
                    return True
                for nei in prereqs[cur]:
                    if nei not in visited:
                        queue.append(nei)
                        visited.add(nei)
            return False

        for pre, post in queries:
            if bfs(pre, post):
                res.append(True)
            else:
                res.append(False)
        return res


"""
Success
Details 
Runtime: 3184 ms, faster than 12.74% of Python3 online submissions for Course Schedule IV.
Memory Usage: 17.6 MB, less than 73.14% of Python3 online submissions for Course Schedule IV.
Next challenges:
All Paths from Source Lead to Destination
Flower Planting With No Adjacent
The Most Similar Path in a Graph
"""
