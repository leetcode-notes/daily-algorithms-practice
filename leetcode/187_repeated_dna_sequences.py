from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        sequences, res = {}, []
        for i in range(len(s)-9):
            cur_sequence = s[i:i+10]
            sequences[cur_sequence] = sequences.get(cur_sequence, 0) + 1
        for k, v in sequences.items():
            if v > 1:
                res.append(k)
        return res


'''
Success
Details
Runtime: 52 ms, faster than 96.65 % of Python3...
Memory Usage: 27.4 MB, less than 43.87 % of Python3...
Next challenges:
Substring with Concatenation of All Words
Subarray Sums Divisible by K
Count Triplets That Can Form Two Arrays of Equal XOR
Show off your acceptance:
'''
