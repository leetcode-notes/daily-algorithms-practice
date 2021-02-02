from collections import Counter


class Solution:
    def subdomainVisits(self, cpdomains):
        table = Counter()
        for data in cpdomains:
            data = data.split(" ")
            count = int(data[0])
            domains = data[1].split(".")
            for i in range(len(domains)):
                domain = ".".join(domains[i:])
                table[domain] += count
        res = []
        for domain, count in table.items():
            output = "{} {}".format(count, domain)
            res.append(output)
        return res


"""
Success
Details 
Runtime: 56 ms, faster than 48.19% of Python3 online submissions for Subdomain Visit Count.
Memory Usage: 14.5 MB, less than 21.08% of Python3 online submissions for Subdomain Visit Count.
Next challenges:
Find All Anagrams in a String
Design HashSet
Powerful Integers
"""
