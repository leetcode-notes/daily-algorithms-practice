from collections import defaultdict


class Solution:
    def killProcess(self, pid, ppid, kill: int):
        graph = defaultdict(set)
        for node, parent in zip(pid, ppid):
            graph[parent].add(node)
        stack = [kill]
        to_kill = set()
        while stack:
            cur_node = stack.pop()
            to_kill.add(cur_node)
            for next_node in graph[cur_node]:
                stack.append(next_node)
        return list(to_kill)


"""
Success
Details 
Runtime: 448 ms, faster than 49.36% of Python3 online submissions for Kill Process.
Memory Usage: 35.1 MB, less than 5.28% of Python3 online submissions for Kill Process.
Next challenges:
Number of Lines To Write String
Moving Stones Until Consecutive II
Find Winner on a Tic Tac Toe Game
"""
