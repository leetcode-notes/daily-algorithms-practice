from collections import deque
from typing import List, Tuple


class Solution:
    def minMutation(self, start: str, end: str, bank) -> int:

        queue = deque()
        queue.append((start, 1))
        visited = set()
        while queue:
            cur_word, dist = queue.popleft()

            for i in range(len(cur_word)):
                for ch in "ACGT":
                    temp_word = cur_word[:i] + ch + cur_word[i+1:]
                    if temp_word in bank and temp_word == end:
                        return dist
                    if temp_word in bank and temp_word not in visited:
                        visited.add(temp_word)
                        queue.append((temp_word, dist+1))
        return -1


"""
Success
Details 
Runtime: 32 ms, faster than 59.48% of Python3 online submissions for Minimum Genetic Mutation.
Memory Usage: 14.2 MB, less than 62.56% of Python3 online submissions for Minimum Genetic Mutation.
Next challenges:
Repeated Substring Pattern
Make Two Arrays Equal by Reversing Sub-arrays
Redistribute Characters to Make All Strings Equal
"""
