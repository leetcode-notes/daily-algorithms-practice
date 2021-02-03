from collections import Counter, defaultdict, deque


class Solution:
    def restoreArray(self, adjacentPairs):
        graph = defaultdict(set)
        counts = Counter()
        for u, v in adjacentPairs:
            counts[u] += 1
            counts[v] += 1
            graph[u].add(v)
            graph[v].add(u)
        queue = deque([])
        seen = set()
        for n in counts:
            if counts[n] == 1:
                seen.add(n)
                queue.append(n)
                break
        res = []
        while queue:
            cur = queue.popleft()
            res.append(cur)
            for nei in graph[cur]:
                if nei not in seen:
                    seen.add(nei)
                    queue.append(nei)
        return res


"""
Success
Details 
Runtime: 1244 ms, faster than 72.38% of Python3 online submissions for Restore the Array From Adjacent Pairs.
Memory Usage: 81.1 MB, less than 18.91% of Python3 online submissions for Restore the Array From Adjacent Pairs.
Next challenges:
Wiggle Subsequence
Non-overlapping Intervals
Group the People Given the Group Size They Belong To
"""
