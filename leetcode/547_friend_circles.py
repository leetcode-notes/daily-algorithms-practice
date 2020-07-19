from collections import defaultdict


class Solution:
    def findCircleNum(self, M):
        friends = defaultdict(set)
        visited = set()

        def dfs(node):
            visited.add(node)
            for friend in friends[node]:
                if friend not in visited:
                    visited.add(friend)
                    dfs(friend)
            return

        for i in range(len(M)):
            for j in range(len(M[0])):
                if i != j:
                    if M[i][j] == 1:
                        friends[i].add(j)
                        friends[j].add(i)
        count = 0
        for i in range(len(M)):
            if i not in visited:
                dfs(i)
                count += 1
        return count


'''
Success
Details
Runtime: 200 ms, faster than 75.15% of Python3
Memory Usage: 15.7 MB, less than 7.47% of Python3
Number of Connected Components in an Undirected Graph
Robot Return to Origin
Sentence Similarity
Sentence Similarity II
The Earliest Moment When Everyone Become Friends
'''
