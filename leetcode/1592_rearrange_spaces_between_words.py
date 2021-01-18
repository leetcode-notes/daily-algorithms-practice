class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaces = 0
        for ch in text:
            if ch == " ":
                spaces += 1
        words = text.split()
        slots = len(words)-1
        amount = 0
        if slots > 0:
            amount = spaces//slots
        leftover = spaces - amount*slots
        res = []
        for i, word in enumerate(words):
            res.append(word)
            if i < len(words)-1:
                res.append(" "*amount)
        res.append(" "*leftover)
        return "".join(res)


"""Success
Details 
Runtime: 28 ms, faster than 79.71% of Python3 online submissions for Rearrange Spaces Between Words.
Memory Usage: 14.2 MB, less than 45.77% of Python3 online submissions for Rearrange Spaces Between Words.
Next challenges:
Text Justification"""
