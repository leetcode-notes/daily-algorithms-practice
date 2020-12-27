from typing import List
from collections import defaultdict, deque


class CountCells:
    def count_leaves(self, nodes_list, kill):
        if not nodes_list:
            return 0
        tree = defaultdict(list)
        for i in range(len(nodes_list)):
            if nodes_list[i] == -1:
                continue
            tree[nodes_list[i]].append(i)
        return self.bfs(tree, nodes_list, kill)

    def bfs(self, tree, nodes_list,  kill):
        queue = deque([0])
        count = 0
        while queue:
            cur = queue.popleft()
            if cur != kill:
                if cur not in tree:
                    count += 1
                else:
                    for child in tree[cur]:
                        queue.append(child)
        return count


t2 = [-1, 0, 0, 2, 2, 4, 4, 6, 6]
kill = 2
parentCell = [-1, 0, 0, 1, 1]
c = CountCells()
t3 = [26, 2, 32, 36, 40, 19, 43, 24, 30, 13, 21, 14, 24, 21, 19, 4, 30, 10, 44, 12, 7, 32, 17, 43,
      35, 18, 7, 36, 10, 16, 5, 38, 35, 4, 13, -1, 16, 26, 1, 12, 2, 5, 18, 40, 1, 17, 38, 44, 14]
print(c.count_leaves(t2, 2))


class CellRemoval:

    def cell_removal(self, parents: List[int], deleted: int) -> int:
        self.res = 0
        for i in range(len(parents)):
            if parents[i] == -1 and i != deleted:
                self.dfs(i, deleted, parents)
        return self.res

    def dfs(self, node, deleted,  parents):
        found = False
        for i in range(len(parents)):
            if parents[i] == node and i != deleted:
                self.dfs(i, deleted, parents)
                found = True
        if not found:
            self.res += 1


'''
s = CellRemoval()
print(s.cell_removal([-1, 0, 0, 1, 1], 6))
#https://community.topcoder.com/stat?c=problem_statement&pm=10275
'''
