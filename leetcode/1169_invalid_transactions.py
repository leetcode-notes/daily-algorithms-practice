from collections import defaultdict


class Solution:
    def invalidTransactions(self, transactions):
        d = defaultdict(list)
        for t in transactions:
            t = t.split(",")
            d[t[0]].append([t[1], t[2], t[3]])

        res = set()
        for k in d:
            if len(d[k]) == 1:
                if int(d[k][0][1]) > 1000:
                    res.add(k+","+",".join(d[k][0]))
                continue
            else:
                for i in range(len(d[k])):
                    cur = d[k][i]
                    if int(cur[1]) > 1000:
                        res.add(k+","+",".join(cur))
                    for j in range(i, len(d[k])):
                        comp = d[k][j]
                        if comp[-1] != cur[-1] and abs(int(comp[0]) - int(cur[0])) <= 60:
                            invalid_0 = k+","+",".join(comp)
                            invalid_1 = k + "," + ",".join(cur)
                            res.add(invalid_0)
                            res.add(invalid_1)
        return list(res)


transactions = ["alice,20,800,mtv", "bob,50,1200,mtv"]
s = Solution()
print(s.invalidTransactions(transactions))


'''
Success
Details
Runtime: 236 ms, faster than 35.71% of Python3
Memory Usage: 14.2 MB, less than 76.37% of Python3
Next challenges:
Remove Duplicates from Sorted Array II
Valid Triangle Number
Max Chunks To Make Sorted II
'''
