import string
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:

        word_set = set(wordList)

        queue = deque()
        queue.append((beginWord, 1))
        visited = set()
        alphabet = string.ascii_lowercase
        while queue:
            cur_word, distance = queue.popleft()

            if cur_word == endWord:
                return distance
            for i in range(len(cur_word)):
                for ch in alphabet:
                    temp_word = cur_word[:i] + ch + cur_word[i+1:]
                    if temp_word in word_set and temp_word not in visited:
                        queue.append((temp_word, distance + 1))
                        visited.add(temp_word)
        return 0


"""
Success
Details 
Runtime: 472 ms, faster than 45.69% of Python3 online submissions for Word Ladder.
Memory Usage: 15.3 MB, less than 67.50% of Python3 online submissions for Word Ladder.
Next challenges:
Word Ladder II
Minimum Genetic Mutation
Show off your acceptance:
"""
