from typing import List
from collections import Counter


class Solution:

    def is_subset(self, l1, l2) -> bool:
        if len(l1) > len(l2):
            return False
        counts = Counter(l2)
        for c in l1:
            if c not in counts:
                return False
        return True

    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        res: List[int] = []
        for i in range(len(favoriteCompanies)):
            curList = favoriteCompanies[i]
            passes = True
            for j in range(len(favoriteCompanies)):
                if j == i:
                    continue
                if self.is_subset(curList, favoriteCompanies[j]):
                    passes = False
                    break
            if passes:
                res.append(i)
        return res


test1 = [["leetcode", "google", "facebook"], ["google", "microsoft"],
         ["google", "facebook"], ["google"], ["amazon"]]
