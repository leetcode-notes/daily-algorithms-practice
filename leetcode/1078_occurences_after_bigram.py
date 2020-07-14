from typing import List


class Solution:
    def findOcurrences(self, text, first: str, second: str) -> List[str]:
        text = text.split(" ")
        res = []
        for i in range(1, len(text)-1):
            if text[i] == second and text[i-1] == first:
                res.append(text[i+1])
        return res


'''
Success
Details
Runtime: 28 ms, faster than 74.29% of Python3
Memory Usage: 13.9 MB, less than 38.41% of Python3
Next challenges:
Shortest Word Distance II
Minimum Index Sum of Two Lists
Design HashMap
'''
