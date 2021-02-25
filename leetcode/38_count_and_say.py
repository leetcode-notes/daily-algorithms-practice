class Solution:
    def countAndSay(self, n: int) -> str:
        start = "1"
        if n == 1:
            return start
        n -= 1
        while n > 0:
            arr = []
            count = 1
            if len(start) == 1:
                arr.append((start, 1))
            for i in range(1, len(start)):
                if start[i] != start[i-1]:
                    arr.append((start[i-1], count))
                    count = 1
                else:
                    count += 1
            if len(start) > 1:
                arr.append((start[-1], count))
            temp = ""
            for num, c in arr:
                temp += str(c)
                temp += str(num)
            start = temp
            n -= 1
        return start


"""
Success
Details 
Runtime: 52 ms, faster than 37.29% of Python3 online submissions for Count and Say.
Memory Usage: 14.6 MB, less than 11.73% of Python3 online submissions for Count and Say.
Next challenges:
Encode and Decode Strings
"""
