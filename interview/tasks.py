from typing import List
# Order a list of words by number of letters but maintain original order
# I think this means primary sort by length,
#  break ties by deferring to original order


def stable_sort_words(word_list) -> List[str]:
    lookup = {}
    lengths = set()
    for word in word_list:
        lengths.add(len(word))
        cur_key = len(word)
        if cur_key in lookup:
            lookup[cur_key].append(word)
        else:
            lookup[cur_key] = [word]
    lengths = sorted(list(lengths), reverse=True)
    res = []
    for length in lengths:
        for word in lookup[length]:
            res.append(word)
    return res


test1 = ["man", "ban", "cat", "apple", "stan", "money"]
# expect [apple, money, stan, man, ban, cat]

print(stable_sort_words(test1))

# print roman numeral equivalent for n in [0, 1000]


class ConvertNumbers:
    def intToRoman(self, num: int) -> str:
        thous, hundreds, tens, ones = 0, 0, 0, 0
        thous = num // 1000
        hundreds = num // 100 % 10
        tens = num // 10 % 10
        ones = num % 10
        res = []
        if thous > 0:
            while thous > 0:
                res.append("M")
                thous -= 1
        if hundreds == 9:
            res.append("CM")
            hundreds -= 9
        if hundreds >= 5:
            res.append("D")
            hundreds -= 5
        if hundreds == 4:
            res.append("CD")
            hundreds -= 4
        for _ in range(hundreds):
            res.append("C")
        if tens == 9:
            res.append("XC")
            tens -= 9
        if tens >= 5:
            res.append("L")
            tens -= 5
        if tens == 4:
            res.append("XL")
            tens -= 4
        for _ in range(tens):
            res.append("X")
        if ones == 9:
            res.append("IX")
            ones -= 9
        if ones >= 5:
            res.append("V")
            ones -= 5
        if ones == 4:
            res.append("IV")
            ones -= 4
        for _ in range(ones):
            res.append("I")
        return "".join(res)


# Implement a stack class

# Stock buy


class BuySellStocks:

    def maxProfitOneTransaction(self, prices):
        if len(prices) <= 1:
            return 0
        minPri, maxPro = prices[0], 0
        for i in range(1, len(prices)):
            minPri = min(minPri, prices[i])
            maxPro = max(maxPro, prices[i]-minPri)
        return maxPro

    def maxProfitUnlimitedTrasactions(self, prices):
        if not prices or len(prices) == 1:
            return 0

        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]

        return profit
