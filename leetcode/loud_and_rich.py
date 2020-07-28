from collections import defaultdict, deque
from functools import lru_cache
from typing import List


class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]):
        graph = defaultdict(set)
        for u, v in richer:
            graph[v].add(u)
        ans = [-1 for _ in range(len(quiet))]

        def dfs(node):
            if ans[node] < 0:
                ans[node] = node
                for child in graph[node]:
                    cand = dfs(child)
                    if quiet[cand] < quiet[ans[node]]:
                        ans[node] = cand
            return ans[node]

        @lru_cache(None)
        def dfs2(node):
            if node not in graph:
                return node
            minimum = node
            for neighbour in graph[node]:
                candidate = dfs(neighbour)
                if quiet[minimum] > quiet[candidate]:
                    minimum = candidate
            return minimum
        for i in range(len(quiet)):
            p = dfs(i)
            ans[i] = p
        return ans

    def loudAndRichTLE(self, richer: List[List[int]], quiet: List[int]):
        graph = defaultdict(set)
        for u, v in richer:
            graph[v].add(u)
        ans = [0 for _ in range(len(quiet))]

        def bfs(node, q):
            queue = deque([node])
            res = node
            while queue:
                cur = queue.popleft()
                if quiet[cur] < q:
                    print(cur)
                    q = quiet[cur]
                    res = cur
                for child in graph[cur]:
                    queue.append(child)
            return res
        for i in range(len(quiet)):
            p = bfs(i, quiet[i])
            ans[i] = p
        return ans


richer = [[1, 0], [2, 1], [3, 1], [3, 7], [4, 3], [5, 3], [6, 3]]
quiet = [3, 2, 5, 4, 6, 1, 7, 0]
s = Solution()
print(s.loudAndRich(richer, quiet))
