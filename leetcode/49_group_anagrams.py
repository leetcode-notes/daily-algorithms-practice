from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        d = defaultdict(list)
        for word in strs:
            word1 = "".join(sorted(word))
            d[word1].append(word)
        return list(d.values())


'''
Success
Details
Runtime: 100 ms, faster than 79.20% of Python3
Memory Usage: 16.7 MB, less than 81.15% of Python3
Next challenges:
Valid Anagram
Group Shifted Strings
'''
