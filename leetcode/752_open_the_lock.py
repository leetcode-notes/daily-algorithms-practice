from collections import deque


class Solution:
    def openLock(self, deadends, target: str) -> int:
        if "0000" in deadends:
            return -1
        if target == "0000":
            return 0
        queue = deque()
        queue.append(["0000", 0])
        visited = set()

        while queue:
            cur, level = queue.popleft()
            new_nums = []
            for i in range(4):
                new_nums.append(
                    cur[:i] + str((int(cur[i])+1) % 10) + cur[i+1:])
                new_nums.append(
                    cur[:i] + str((int(cur[i])-1) % 10) + cur[i+1:])

            for num in new_nums:
                if num in visited or num in deadends:
                    continue
                visited.add(num)
                if num == target:
                    return level + 1
                queue.append([num, level+1])
        return -1


"""
Success
Details
Runtime: 1144 ms, faster than 23.85 % of Python3 online submissions for Open the Lock.
Memory Usage: 15.3 MB, less than 83.58 % of Python3 online submissions for Open the Lock.
Next challenges:
Walls and Gates
Minimum Height Trees
Vertical Order Traversal of a Binary Tree
"""
