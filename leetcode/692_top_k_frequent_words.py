from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0)+1

        count_word = defaultdict(list)
        for w, v in word_count.items():
            count_word[v].append(w)
        max_freq = len(words)
        res = []
        while max_freq > 0:
            if max_freq in count_word:
                for w in sorted(count_word[max_freq]):
                    if k == 0:
                        return res
                    res.append(w)
                    k -= 1
            max_freq -= 1
        return res


'''
Success
Details
Runtime: 48 ms, faster than 97.26% of Python3...
Memory Usage: 14 MB, less than 32.20% of Python3...
Next challenges:
Race Car
Array of Doubled Pairs
Vertical Order Traversal of a Binary Tree
'''
