class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split(" ")
        length = len(searchWord)
        for i, word in enumerate(sentence):
            if len(word) < len(searchWord):
                continue
            if searchWord == word[0:length]:
                return i+1
        return -1


s = Solution()
print(s.isPrefixOfWord("i love eating burger",
                       "burg"))
