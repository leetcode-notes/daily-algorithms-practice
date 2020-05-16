class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = {}
        for i in range(1, n+1):
            d = self.digitSum(i)
            groups[d] = 1 if d not in groups else groups[d]+1
        largest = 0 
        count = 0
        for k, v in groups.items():
            if v > largest:
                count = 1 
                largest = v 
            elif v == largest:
                count += 1 
        return count

    def digitSum(self, num):
        n = str(num)
        total = 0
        for c in n:
            total += int(c)
        return total
