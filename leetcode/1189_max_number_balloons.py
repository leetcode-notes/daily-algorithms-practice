from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = Counter("balloon")
        text_char_count = Counter(text)
        max_balloons = len(text)//7
        for k, v in text_char_count.items():
            if k in balloon:
                req = balloon[k]
                max_balloons = min(max_balloons, (v//req))
        return max_balloons


test1 = "nlaebolko"
test2 = "loonbalxballpoon"
s = Solution()
print(s.maxNumberOfBalloons(test2))

'''
Success
Details
Runtime: 36 ms, faster than 47.88%....
Memory Usage: 13.8 MB, less than 59.16%...
Next challenges:
Sudoku Solver
Split Concatenated Strings
Subarray Sum Equals K
'''
