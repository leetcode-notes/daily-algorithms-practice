from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        counts = {}
        for start, end in paths:
            counts[start] = 1 if start not in counts else counts[start]+1
            if end not in counts:
                counts[end] = 0 
        for k, v in counts.items():
            if v == 0:
                return k 


paths = [["B","C"],["D","B"],["C","A"]]

s = Solution()
print(s.destCity(paths))