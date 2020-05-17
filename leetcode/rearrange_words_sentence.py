from collections import defaultdict


class Solution:
    def arrangeWords(self, text) -> str:
        words = defaultdict(list)
        lengths = []
        text = text.split(" ")
        for word in text:
            word = word.lower()
            words[len(word)].append(word)
            lengths.append(len(word))
        lengths.sort()
        res = []
        for length in lengths:
            for word in words[length]:
                res.append(word)
            del words[length]
        res[0] = res[0].capitalize()
        return " ".join(w for w in res)


s = Solution()
print(s.arrangeWords("keep calm and code on"))
