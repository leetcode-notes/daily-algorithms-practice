from collections import defaultdict


class Solution:
    def makeConnected(self, n, connections):
        if len(connections) < n-1:
            return -1
        graph = defaultdict(set)
        for u, v in connections:
            graph[u].add(v)
            graph[v].add(u)
        seen = set()

        def dfs(start):
            for neigh in graph[start]:
                if neigh not in seen:
                    seen.add(neigh)
                    dfs(neigh)
        count = 0
        for i in range(n):
            if i not in seen:
                seen.add(i)
                dfs(i)
                count += 1
        return count-1


s = Solution()
print(s.makeConnected(5, [[0, 1], [0, 2], [3, 4], [2, 3]]))
